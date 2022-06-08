from enum import Enum

DATE_FORMAT_STRING = '%d/%m/%Y'
DEFAULT_STATS = {
            'Mediana': 0,
            'Dominanta': 0,
            'Odchylenie standardowe': 0,
            'Współczynnik zmienności': 0
        }

DEFAULT_SESSION_DATA = {
            'Rosnące': 0,
            'Malejące': 0,
            'Bez zmian': 0,
        }
STYLES = """
            QLabel {
                font-size: 20px;
                font-weight: 300;
            }
            QPushButton {
                font-size: 24px;
                font-weight: 400;
                padding: 10px;
            }
            QComboBox {
                font-size: 18px;
                font-weight: 300;
            }
            QTableWidget {
                font-size: 16px;
                font-weight: 300;
            }
            QHeaderView {
                font-size: 18px;
                font-weight: 300;
            }
        """
class Currency(Enum):
    PLN = 0
    USD = 1
    EUR = 2
    GBP = 3
    JPY = 4
    CHF = 5

class Period(Enum):
    ONE_WEEK = 0, 7, 'Tydzień'
    TWO_WEEK = 1, 14, 'Dwa tygodnie'
    MONTH = 2, 30, 'Miesiąc'
    QUARTER = 3, 90, 'Kwartał'
    YEAR = 4, 365, 'Rok'

    def getValue(value):
        print
        if Period['ONE_WEEK'].value[0] == value:
            return Period.ONE_WEEK
        elif Period['TWO_WEEK'].value[0] == value:
            return Period.TWO_WEEK
        elif Period['MONTH'].value[0] == value:
            return Period.MONTH
        elif Period['QUARTER'].value[0] == value:
            return Period.QUARTER
        elif Period['YEAR'].value[0] == value:
            return Period.YEAR
        else:
            return None