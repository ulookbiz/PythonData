# Класс "Свеча"
class candle():

# --------------------------------
#   Инициализатор
    def __init__(self,timeframe):

# типы свеч: "m1","m5","m15","m30","h1","h4","d1","M1"
# дополнительно: "m10","m20","h2","h6","h12"
        self.tf = timeframe # тип свечи
        self.high = None
        self.low = None
        self.open = None
        self.close = None
        self.volume = 0
        self.year = None
        self.month = None
        self.day = None
        self.hour = None
        self.upFr = False # признак up-фрактала
        self.downFr = False # признак down-фрактала
        self.prev = None # объект предыдущей свечи
        self.next = None # объект следующей свечи
        self.ticks = 0 # количество тиков

        return

#---------------------------------
#   Метод учета очередного тика
#   Параметр - тик
#   Формат: { 'year': , 'month': , 'day': , 'hour': ,
#             'min': , 'sec': , 'bid': , 'ask': }
    def add(self,tick,quantity):

#        if(self.tf == 'm1'):
#            print(tick)

        bid = tick['bid']

        if(self.open == None):
            self.open = bid
            self.year = tick['year']
            self.month = tick['month']
            self.day = tick['day']
            if(self.tf == "h1"):
                self.hour = tick['hour']
            if(self.tf == "m1"):
                self.hour = tick['hour']
                self.minu = tick['min']
        self.close = bid
        self.volume += 1
        if(self.high == None):
            self.high = bid
        elif(self.high < bid):
            self.high = bid
        if(self.low == None):
            self.low = bid
        elif(self.low > bid):
            self.low = bid
            
        self.ticks += quantity

        return self

#---------------------------------
#   Метод завершения формирования свечи
    def complete(self):

#        print(self.tf)
        pass
        return