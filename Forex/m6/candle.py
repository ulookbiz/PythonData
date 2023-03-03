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
        self.minute = None
        self.upFr = False # признак up-фрактала
        self.downFr = False # признак down-фрактала
        self.prev = None # объект предыдущей свечи
        self.next = None # объект следующей свечи
        self.ticks = 0 # количество тиков
        self.spread = None

        return

#---------------------------------
#   Метод учета очередного тика
#   Параметр - тик
#   Формат: { 'year': , 'month': , 'day': , 'hour': ,
#             'min': , 'sec': , 'bid': , 'ask': }
    def add(self,tick,quantity):

        bid = tick['bid']

        if(self.open == None):
            self.open = bid
            self.year = tick['year']
            self.month = tick['month']
            self.day = tick['day']
            self.hour = 0
            self.minute = 0
            if(self.tf == "h1"):
                self.hour = tick['hour']
            if(self.tf == "m1"):
                self.hour = tick['hour']
                self.minute = tick['min']
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
#   Метод создания готовой свечи
    def ready(self,p):
        
#       примечание: параметр p[0] - id в базе данных, не нужен
        self.low = p[1]
        self.high = p[2]
        self.open = p[3]
        self.close = p[4]
        self.year = p[5]
        self.month = p[6]
        self.day = p[7]
        if(self.tf == 'd1'):
            self.hour = 0
            self.minute = 0
            self.volume = p[8]        
            self.spread = p[9]
        elif(self.tf == 'h1'):
            self.hour = p[8]
            self.minute = 0
            self.volume = p[9]        
            self.spread = p[10]
        elif(self.tf == 'm1'):
            self.hour = p[8]
            self.minute = p[9]
            self.volume = p[10]        
            self.spread = p[11]
            
        return

#---------------------------------
#   Метод завершения формирования свечи
    def complete(self):

#        print("Свеча open: ",self.open," close: ",self.close)
        pass
        return
    
# --------------------------------
#   Метод распечатки данных свечи
    def dump(self,i):
        
        print("___Свеча___ ",i,". ")
        print("Low: ", self.low, " High: ", self.high, " Open: ", self.open, " Close: ", self.close)
        print("Месяц: ", self.month, " День: ", self.day, " Час: ", self.hour, " Минута: ", self.minute)
        
        return