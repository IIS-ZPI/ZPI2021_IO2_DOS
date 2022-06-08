from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QComboBox,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMainWindow,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QAbstractScrollArea,
    QSizePolicy,
    QHeaderView
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from analysis import Analysis
from dataTypes import DATE_FORMAT_STRING, DEFAULT_SESSION_DATA, DEFAULT_STATS, Currency, Period

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.mainWidget = MainWidget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Analiza par walutowych')
        self.setCentralWidget(self.mainWidget)
        self.setGeometry(0, 0, 1200, 600)
        self.showMaximized()
        self.show()

class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.analysis = Analysis(Currency.EUR, Currency.PLN, Period.ONE_WEEK)
        self.initUI()
        self.formatter = mdates.DateFormatter(DATE_FORMAT_STRING)

    def initUI(self):   
        grid = QGridLayout()

        dataInputLayout = QVBoxLayout()
        dataInputLayout.addStretch(4)
        appName = QLabel('Analiza par walutowych')
        appName.setStyleSheet('font-size: 28px')
        dataInputLayout.addWidget(appName, alignment=Qt.AlignCenter)
        dataInputLayout.addStretch(4)
        dataInputLayout.addWidget(QLabel('Wprowadź pierwszą walutę:'))
        self.firstCurrencyCombo = QComboBox()
        self.firstCurrencyCombo.addItems([currency.name for currency in Currency])
        self.firstCurrencyCombo.setCurrentIndex(Currency.EUR.value)
        dataInputLayout.addWidget(self.firstCurrencyCombo)
        dataInputLayout.addStretch(1)

        dataInputLayout.addWidget(QLabel('Wprowadź drugą walutę:'))
        self.secondCurrencyCombo = QComboBox()
        self.secondCurrencyCombo.addItems([currency.name for currency in Currency])
        self.secondCurrencyCombo.setCurrentIndex(Currency.PLN.value)
        dataInputLayout.addWidget(self.secondCurrencyCombo)
        dataInputLayout.addStretch(1)
        
        dataInputLayout.addWidget(QLabel('Wprowadź okres:'))
        self.periodCombo = QComboBox()
        self.periodCombo.addItems([period.value[2] for period in Period])
        dataInputLayout.addWidget(self.periodCombo)
        dataInputLayout.addStretch(1)
        
        self.analyzeButton = QPushButton('ANALIZUJ')
        self.analyzeButton.clicked.connect(self.analyze)
        dataInputLayout.addWidget(self.analyzeButton)
        dataInputLayout.addStretch(6)
        dataInputLayout.addWidget(QLabel('Informacje o sesjach'))
        self.tableWidget = QTableWidget()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.tableWidget.setRowCount(3) 
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Rodzaj sesji', '    Liczba    '])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        dataInputLayout.addWidget(self.tableWidget)
        dataInputLayout.addStretch(1)
        
        dataInputLayout.addWidget(QLabel('Statystyka'))
        self.tableWidget2 = QTableWidget()
        self.tableWidget2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.tableWidget2.setRowCount(4) 
        self.tableWidget2.setColumnCount(2)
        self.tableWidget2.setHorizontalHeaderLabels(['Miara statystyczna', '    Wartość    '])
        self.tableWidget2.verticalHeader().setVisible(False)
        self.tableWidget2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget2.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        self.fillTable(DEFAULT_SESSION_DATA, DEFAULT_STATS)
        dataInputLayout.addWidget(self.tableWidget2)
        dataInputLayout.addStretch(4)
        dataInput = QWidget(self)
        dataInput.setLayout(dataInputLayout)
        grid.addWidget(dataInput, 0, 0, 2, 1)


        self.mainChart = FigureCanvas(plt.Figure(figsize=(15, 6)))
        self.mainChartFigure = None
        grid.addWidget(self.mainChart, 0, 1)

        self.secondChart = FigureCanvas(plt.Figure(figsize=(15, 3)))
        self.secondChartFigure = None
        grid.addWidget(self.secondChart, 1, 1)
        self.setLayout(grid)

    def analyze(self):
        self.analysis.mainCurrency = Currency(self.firstCurrencyCombo.currentIndex())
        self.analysis.secondCurrency = Currency(self.secondCurrencyCombo.currentIndex())
        self.analysis.period = Period.getValue(self.periodCombo.currentIndex())
        self.analysis.analyze()

        if self.mainChartFigure:
            self.mainChartFigure.remove()
        self.mainChartFigure = self.mainChart.figure.subplots()

        title, values = self.analysis.getCurrencyValueInTime()
        self.mainChartFigure.plot([day for day, _ in values], [value for _, value in values])
        self.mainChartFigure.set_title(title)
        self.mainChartFigure.xaxis.set_major_formatter(self.formatter)
        self.mainChart.draw()

        if self.secondChartFigure:
            self.secondChartFigure.remove()
        self.secondChartFigure = self.secondChart.figure.subplots()

        title, values = self.analysis.getMonthlyChanges()
        barlist = self.secondChartFigure.bar([day for day, _ in values], [value for _, value in values])
        for bar in barlist:
            if bar._height > 0:
                bar.set_color('g')
            elif bar._height < 0:
                bar.set_color('r')
            else:
                bar.set_color('k')
        self.secondChartFigure.set_title(title)
        self.secondChart.draw()

        self.fillTable(self.analysis.getNumberOfSessions(), self.analysis.getStatistics())

    def fillTable(self, sessionsData: dict, statsData: dict):
        print(sessionsData, statsData)
        index = 0
        for k, v in sessionsData.items():
            tempKey = QTableWidgetItem()
            tempKey.setText(k)
            tempKey.setFlags(Qt.ItemIsEnabled)
            tempValue = QTableWidgetItem()
            tempValue.setText(str(v))
            tempValue.setFlags(Qt.ItemIsEnabled)
            self.tableWidget.setItem(index, 0, tempKey)
            self.tableWidget.setItem(index, 1, tempValue)
            index += 1
        index = 0
        for k, v in statsData.items():
            tempKey = QTableWidgetItem()
            tempKey.setText(k)
            tempKey.setFlags(Qt.ItemIsEnabled)
            tempValue = QTableWidgetItem()
            tempValue.setText(str(v))
            tempValue.setFlags(Qt.ItemIsEnabled)
            self.tableWidget2.setItem(index, 0, tempKey)
            self.tableWidget2.setItem(index, 1, tempValue)
            index += 1