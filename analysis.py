from dataTypes import DATE_FORMAT_STRING, Period, Currency
from datetime import datetime
class Analysis:
    def __init__(self, mainCurrency: Currency, secondCurrency: Currency, period: Period) -> None:
        self.mainCurrency = mainCurrency
        self.secondCurrency = secondCurrency
        self.period = period
    
    def analyze(self):
        # update output of 'get' methods print only for testing
        print(self.mainCurrency)
        print(self.secondCurrency)
        print(self.period)

    def getCurrencyValueInTime(self):
        sampleData = [
            (datetime(2017, 1, 1), 123.12), 
            (datetime(2017, 1, 2), 121.32), 
            (datetime(2017, 1, 3), 111.32), 
            (datetime(2017, 1, 4), 125.32), 
            (datetime(2017, 1, 5), 127.32), 
            (datetime(2017, 1, 6), 127.32), 
            (datetime(2017, 1, 7), 127.32), 
            (datetime(2017, 1, 8), 127.32), 
            (datetime(2017, 1, 9), 127.32), 
            (datetime(2017, 1, 10), 127.32), 
            (datetime(2017, 1, 11), 127.32), 
            ]
        return f'{self.mainCurrency.name} {self.secondCurrency.name} {sampleData[0][0].strftime(DATE_FORMAT_STRING)} - {sampleData[-1][0].strftime(DATE_FORMAT_STRING)}', sampleData

    def getNumberOfSessions(self):
        return {
            'Rosnące': 12,
            'Malejące': 2,
            'Bez zmian': 3,
        }

    def getStatistics(self):
        return {
            'Mediana': 10,
            'Dominanta': 2,
            'Odchylenie standardowe': 2.44,
            'Współczynnik zmienności': 1.23
        }
    
    def getMonthlyChanges(self):
        sampleData = [
            ('01/03/2022', 1.12), 
            ('01/04/2022', -3.32), 
            ('01/05/2022', -2.9), 
            ('01/06/2022', 3.51), 
            ('01/07/2022', 0), 
            ('01/08/2022', 5.2), 
            ]
        return 'chart-title', sampleData