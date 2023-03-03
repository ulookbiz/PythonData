# Класс "Свеча"
class candle():

# --------------------------------
#   Инициализатор
    def __init__(self,type):

        self.type = type # тип свечи
        self.high = None
        self.low = None
        self.open = None
        self.close = None
        self.volume = 0
        self.closed = False # признак окончания формирования свечи
        self.direction = 0 # признак свечи - вверх(1), вниз(-1), никуда(0)
        self.volat_up = 0
        self.volat_down = 0
        return

#---------------------------------
#   Метод приема порции информации
    def put(self,data):

        self.volume += data['volume']
        bid = data['bid']

#       учет волатильности
        if(self.close != None):
            if(bid > self.close):
                self.volat_up += 1
            elif(bid < self.close):
                self.volat_down += 1

#       обновление данных
        self.close = bid
        if(self.open == None):
            self.open = bid
            self.high = bid
            self.low = bid
        else:
            if(bid > self.high):
                self.high = bid
            elif(bid < self.low):
                self.low = bid

#       направление свечи
        self.direction = 0
        if(bid > self.open):
            self.direction = 1
        elif(bid < self.open):
            self.direction = -1

        return

#---------------------------------
#   Метод завершения формирования свечи
    def cclose(self):

        self.closed = True
        return

#---------------------------------
#   Метод выдачи данных свечи
    def get(self):
        
        return {
            "high": self.high,
            "low": self.low,
            "open": self.open,
            "close": self.close,
            "direction": self.direction,
            "volume":self.volume
               }


# Класс "Свеча M1"
class M1candle(candle):
# --------------------------------
#   Инициализатор
    def __init__(self):
        super().__init__("M1")
        return

# Класс "Свеча H1"
class H1candle(candle):
# --------------------------------
#   Инициализатор
    def __init__(self):
        super().__init__("H1")
        return


# Класс "Свеча D1"
class D1candle(candle):
# --------------------------------
#   Инициализатор
    def __init__(self):
        super().__init__("D1")
        return