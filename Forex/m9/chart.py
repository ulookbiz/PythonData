import MetaTrader5 as mt5
from candle import candle
from funcs import ttime
from pattern import pattern
from plot import plot

# Класс "График"
class chart():

# --------------------------------
#   Инициализатор
    def __init__(self,timeframe,chart_width):

        self.timef = timeframe
        if(self.timef == 'd1'):
            self.timeframe = mt5.TIMEFRAME_D1
        elif(self.timef == 'h4'):
            self.timeframe = mt5.TIMEFRAME_H4
        elif(self.timef == 'h1'):
            self.timeframe = mt5.TIMEFRAME_H1
        elif(self.timef == 'm30'):
            self.timeframe = mt5.TIMEFRAME_M30
        elif(self.timef == 'm15'):
            self.timeframe = mt5.TIMEFRAME_M15
        elif(self.timef == 'm5'):
            self.timeframe = mt5.TIMEFRAME_M5
        elif(self.timef == 'm1'):
            self.timeframe = mt5.TIMEFRAME_M1
        self.quantity = chart_width # количество свечей, допустимое для хранения в объекте
#       массив свечей, в котором самые новые свечи - в начале массива        
        self.candles = []
#       ctime, btime - переменные, отображающие временны'е границы графика
#       None Означает отсутствие каких-либо данных      
        self.ctime = None # Текущее (последнее) значение времени
        self.btime = None # Начальное значение времени
#       текущий день или час или минута для учета тиков
        self.cdhm = None
        self.plot = plot()

#       отладка
        self.cnt = 0

        return

# --------------------------------
#   Метод добавления элемента (свечи) в массив
    def add(self,el):

        if(len(self.candles) == self.quantity):
#           удаление последнего элемента            
            self.candles.pop(self.quantity-1)
#       добавление в начало списка со сдвигом вправо            
        self.candles.insert(0,el)
#       проверка фрактала для свечи [2]
        self.fractal()

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
        elif(self.timef == 'h4'):
#           определяющее - начало часа
            tmp = time1.hour%4
            check = time1.hour-tmp
        elif(self.timef == 'h1'):
            check = time1.hour
        elif(self.timef == 'm30'):
#           определяющее - начало минуты
            tmp = time1.minute%30
            check = time1.minute-tmp
        elif(self.timef == 'm15'):
#           определяющее - начало минуты
            tmp = time1.minute%15
            check = time1.minute-tmp
        elif(self.timef == 'm5'):
#           определяющее - начало минуты
            tmp = time1.minute%5
            check = time1.minute-tmp
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
#            length = len(self.candles)
#            cndl = self.candles[length-1]
            cndl = self.candles[0]
            cndl.add(tick,quantity)
        else:
#           завершение предыдущей свечи
            length = len(self.candles)
            if(length > 0):
                cndl = self.candles[0]
                cndl.complete()
#               проверка фрактала для свечи [2]
#                self.fractal()

#           начало формирования новой свечи
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
        elif(self.timef == 'h4'):
            tmp = newcndl.hour%4
            self.cdhm = newcndl.hour-tmp
        elif(self.timef == 'h1'):
            self.cdhm = newcndl.hour
        elif(self.timef == 'm30'):
            tmp = newcndl.minute%30
            self.cdhm = newcndl.minute-tmp
        elif(self.timef == 'm15'):
            tmp = newcndl.minute%15
            self.cdhm = newcndl.minute-tmp
        elif(self.timef == 'm5'):
            tmp = newcndl.minute%5
            self.cdhm = newcndl.minute-tmp
        elif(self.timef == 'm1'):
            self.cdhm = newcndl.minute

        return

# --------------------------------
#   Метод проверки свойства свечи "фрактал"
    def fractal(self,ind=2):

        if(len(self.candles) < ind+3):
            return

        cndl = self.candles[ind]        
#       проверка верхнего фрактала
        if(cndl.high > self.candles[ind-1].high):
            if(cndl.high > self.candles[ind-2].high):
                if(cndl.high > self.candles[ind+1].high):
                    if(cndl.high > self.candles[ind+2].high):
                        cndl.upFr = True
#       проверка нижнего фрактала
        if(cndl.low < self.candles[ind-1].low):
            if(cndl.low < self.candles[ind-2].low):
                if(cndl.low < self.candles[ind+1].low):
                    if(cndl.low < self.candles[ind+2].low):
                        cndl.downFr = True
                        
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
            self.plot.trade_put(cndl.open,cndl.close,cndl.high,cndl.low,cndl.volume)

        self.plot.plot()

        return

# --------------------------------
#   Метод отрисовки части графика
    def part_plot(self,p1,p2):

        for cndl in self.candles[p1:p2:-1]:
            self.plot.time_put(cndl.year,cndl.month,cndl.day,cndl.hour,cndl.minute)
            self.plot.trade_put(cndl.open,cndl.close,cndl.high,cndl.low,cndl.volume)

        self.plot.plot()

        return

# --------------------------------
#   Метод создания и отрисовки изоморфного графика
    def chart_iso(self,n=None):

        if(n == None):
            n = len(self.candles)

        self.plot = plot()
        pat = pattern()
        i = 0
        for cndl in reversed(self.candles):
            pat.add(cndl.open)
            pat.add(cndl.close)
            pat.add(cndl.high)
            pat.add(cndl.low)
            i += 1
#            print(i)
            if(i == n):
                break

        i = 0
        patt = pat.iso(n*4)
        
#        print(patt)
        
        for cndl in reversed(self.candles):
            self.plot.time_put(cndl.year,cndl.month,cndl.day,cndl.hour,cndl.minute)
            op = patt[i*4]
            cl = patt[i*4+1]
            hi = patt[i*4+2]
            lo = patt[i*4+3]
            self.plot.trade_put(op,cl,hi,lo,cndl.volume)
            i += 1
            if(i == n):
                break
           
#            print(op,cl,hi,lo)
#            print(cl)

        self.plot.plot()
        
        return pat
