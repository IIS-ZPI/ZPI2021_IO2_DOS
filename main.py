import sys
from PyQt5.QtWidgets import QApplication
from dataTypes import STYLES
from gui import GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLES)
    ex = GUI()
    sys.exit(app.exec_())
