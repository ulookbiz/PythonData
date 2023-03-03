import MetaTrader5 as mt5
from candle import candle
from funcs import ttime
from plot import plot

# Класс "График"
class chart():

# --------------------------------
#   Инициализатор
    def __init__(self,timeframe,chart_width):

        self.timef = timeframe
        if(self.timef == 'd1'):
            self.timeframe = mt5.TIMEFRAME_D1
        elif(self.timef == 'h1'):
            self.timeframe = mt5.TIMEFRAME_H1
        elif(self.timef == 'm1'):
            self.timeframe = mt5.TIMEFRAME_M1
        self.quantity = chart_width # количество свечей, хранимых в объекте
        self.candles = []
#       ctime, btime - переменные, отображающие временны'е границы графика
#       None Означает отсутствие каких-либо данных      
        self.ctime = None # Текущее (последнее) значение времени
        self.btime = None # Начальное значение времени
#       текущий день или час или минута для учета тиков
        self.cdhm = None
        self.plot = plot()

        return

# --------------------------------
#   Метод добавления элемента (свечи) в массив
    def add(self,el):

        if(len(self.candles) == self.quantity):
#           удаление последнего элемента            
            self.candles.pop(self.quantity-1)
#       добавление в начало списка со сдвигом вправо            
        self.candles.insert(0,el)

#        print(el.day)
        return

# --------------------------------
#   Метод учета тика
#   Параметр - тик
#   Формат: { 'year': , 'month': , 'day': , 'hour': ,
#             'min': , 'sec': , 'bid': , 'ask': }
    def put(self,tick,quantity):

        time1 = ttime(tick['year'],tick['month'],tick['day'],tick['hour'],tick['min'],tick['sec'])
        if(self.timef == 'd1'):
            check = time1.day
        elif(self.timef == 'h1'):
            check = time1.hour
        elif(self.timef == 'm1'):
            check = time1.minute
            
        if(self.btime == None):
#           это старт формирования первой свечи
#           но это может быть только при полном отсутствии предыдущих свечей
            cndl = candle(self.timef)
            self.candles.append(cndl)
            self.cdhm = check
#           начальное время графика            
            self.btime = time1
            
        if(check == self.cdhm):
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
            self.add(cndl)
            self.cdhm = check

#       обновление текущего времени с каждым тиком    
        self.ctime = time1

        return

# --------------------------------
#   Метод добавления в учет готовой свечи
    def candleAdd(self,cndl_data):
        
        newcndl = candle(self.timef) # создание свечи
        newcndl.ready(cndl_data)     # заполнение свечи
        time1 = ttime(newcndl.year,newcndl.month,newcndl.day,newcndl.hour,newcndl.minute,0)
        self.add(newcndl)            # включение свечи в массив
        if(self.btime == None):
#           первая свеча формирует начало диапазона и текущее окончание
            self.btime = time1
        self.ctime = time1                   

        if(self.timef == 'd1'):
            self.cdhm = newcndl.day
        elif(self.timef == 'h1'):
            self.cdhm = newcndl.hour
        elif(self.timef == 'm1'):
            self.cdhm = newcndl.minute
            
        return
    
# --------------------------------
#   Метод распечатки состояния графика
    def dump(self):
        
        print(" ")
        print("***************************")
        print(len(self.candles))
        print("Timeframe: ",self.timef)
        print("Максимальное количество свечей: ",self.quantity)
        print("Текущее количество свечей: ",len(self.candles))
        if(len(self.candles) > 0):
            print("Начало графика:",self.btime)
            print("Окончание графика:",self.ctime)
#            print("Последняя свеча:")
#            self.candles[0].dump(0)
        else:
            print("График не содержит данных")
        
        print("----------- Все свечи: -----------")
        print(" ")
        i=1
        for cndl in self.candles:
            cndl.dump(i)
            i += 1
        print("--------------------------")
        
        return

# --------------------------------
#   Метод отрисовки графика
    def chart_plot(self):

        for cndl in reversed(self.candles):
            self.plot.time_put(cndl.year,cndl.month,cndl.day,cndl.hour,cndl.minute)
            self.plot.trade_put(cndl.open,cndl.close,cndl.high,cndl.close,cndl.volume)

        self.plot.plot()

        return        

# --------------------------------
#   Метод отрисовки скоростей, эксперимент
    def chart_speed(self):

#        lng = len(self.candles)
#        for i in range(lng-1,1,-1):
        for cndl in reversed(self.candles):
#            cndl = self.candles[i]
#            cndl2 = self.candles[i-1]
            open1 = 0
            close = cndl.close - cndl.open
            high = 0
            low = 0
            volume = cndl.volume
            self.plot.time_put(cndl.year,cndl.month,cndl.day,cndl.hour,cndl.minute)
            self.plot.trade_put(open1,close,high,low,volume)

        self.plot.plot()

        return        
