# Класс "Свеча"
class candle():

# --------------------------------
#   Инициализатор
    def __init__(self,type):

# типы свеч: "m1","m5","m15","m30","h1","h4","d1","M1"
# дополнительно: "m10","m20","h2","h6","h12"
        self.type = type # тип свечи
        self.high = None
        self.low = None
        self.open = None
        self.close = None
        self.volume = 0
        self.year = None
        self.month = None
        self.day = None
        self.direction = 0 # признак свечи - вверх(1), вниз(-1), никуда(0)
        self.upFr = False # признак up-фрактала
        self.downFr = False # признак down-фрактала
        self.prev = None # объект предыдущей свечи
        self.next = None # объект следующей свечи

        return

#---------------------------------
#   Метод формирования свечи массивом данных:
#   id,low,high,open,close,year,month,day,volume
    def d1Candle(self,data):

        self.low = data[1]
        self.high = data[2]
        self.open = data[3]
        self.close = data[4]
        self.year = data[5]
        self.month = data[6]
        self.day = data[7]
        self.volume = data[8]

        return self

#---------------------------------
#   Метод формирования свечи массивом данных:
#   id,low,high,open,close,year,month,day,volume
    def h1Candle(self,data):

        self.low = data[1]
        self.high = data[2]
        self.open = data[3]
        self.close = data[4]
        self.year = data[5]
        self.month = data[6]
        self.day = data[7]
        self.hour = data[8]
        self.volume = data[9]

        return self
