from candle import candle

# Класс "График"
class chart():

# --------------------------------
#   Инициализатор
    def __init__(self,timeframe):

        self.timef = timeframe
        self.candles = []
        self.ctime = None

        return

# --------------------------------
#   Метод учета тика
#   Параметр - тик
#   Формат: { 'year': , 'month': , 'day': , 'hour': ,
#             'min': , 'sec': , 'bid': , 'ask': }
    def put(self,tick,quantity):

        if(self.timef == "m1"):
            krit = tick['min']
        elif(self.timef == "h1"):
            krit = tick['hour']
        else:
            krit = tick['day']
                

        if(self.ctime == None):
#           это старт формирования первой свечи
            cndl = candle(self.timef)
            self.candles.append(cndl)
            self.ctime = krit

        if(krit == self.ctime):
#           дополнение данных свечи
            length = len(self.candles)
            cndl = self.candles[length-1]
            cndl.add(tick,quantity)
        else:
#           завершение предыдущей свечи
            length = len(self.candles)
            if(length > 0):
                cndl = self.candles[length-1]
                cndl.complete()
#           формирование новой свечи
            cndl = candle(self.timef)
            cndl.add(tick,quantity)
            self.candles.append(cndl)
            self.ctime = krit

        return
