from funcs import ttime
from candle import candle

#....................................
# Класс "Charter"
# Организатор работы всей группы графиков одновременно
#....................................

class Charter():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,pairs,timeframes,chart_width):
        
        self.charts = dict()
        for pair in pairs:
            self.charts[pair] = dict()
            for timeframe in timeframes:
                if(timeframe == 'm1'):
                    self.charts[pair][timeframe] = M1Chart(pair,chart_width)

# --------------------------------
#   метод добавления группы свечей
#   переопределяет формат данных в формат свечей
    def add(self,pair,timeframe,data):

        chart = self.charts[pair][timeframe]
        length = len(data['low'])
        
        for i in range(length):
            cndl = {}
            cndl['low'] = data['low'][i]
            cndl['high'] = data['high'][i]
            cndl['open'] = data['open'][i]
            cndl['close'] = data['close'][i]
            cndl['year'] = data['time'].dt.year[i]
            cndl['month'] = data['time'].dt.month[i]
            cndl['day'] = data['time'].dt.day[i]
            cndl['hour'] = 0
            cndl['minute'] = 0
            cndl['tick_volume'] = data['tick_volume'][i]
            cndl['spread'] = data['spread'][i]
            if(timeframe != 'd1'):
                cndl['hour'] = data['time'].dt.hour[i]
                if(timeframe != 'h1'):
                    cndl['minute'] = data['time'].dt.minute[i]
            chart.candleAdd(cndl)
        
        return

# --------------------------------
#   метод приема тика с данными рассылка по таймфреймам
    def put(self,pair,tick):

        for ch in self.charts[pair]:
            ch.put(tick)

# --------------------------------
#   метод выполнения обобщения
    def generalization(self,timeframe):
        
        print("Charter: generalization")
        pass



#=========================================
# Класс графика "Chart"
class Chart():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,pair,chart_width):
        
        self.pair = pair
        self.chart_width = chart_width
#       массив свечей, в котором самые новые свечи - в начале массива        
        self.candles = []
#       ctime, btime - переменные, отображающие временны'е границы графика
        self.btime = self.ctime = None

# --------------------------------
#   Метод добавления в учет готовой свечи
    def candleAdd(self,cndl_data):

        newcndl = candle(self.timeframe) # создание свечи
        newcndl.ready(cndl_data)     # заполнение свечи
        time1 = ttime(newcndl.year,newcndl.month,newcndl.day,newcndl.hour,newcndl.minute,0)
        self.candles.append(newcndl)            # включение свечи в массив

        if(self.btime == None):
#           первая свеча формирует начало диапазона и текущее окончание
            self.btime = time1
        self.ctime = time1                   

        return

# --------------------------------
#   Метод добавления элемента (свечи) в массив
    def add(self,el):

        if(len(self.candles) == self.chart_width):
#           удаление последнего элемента            
            self.candles.pop(self.chart_width-1)
#       добавление в начало списка со сдвигом вправо            
        self.candles.insert(0,el)

        return

        
#=========================================        
# Класс графика "M1Chart"
class M1Chart(Chart):
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,pair,chart_width):

        super().__init__(pair,chart_width)
        self.current = None # текущая минута
        self.timeframe = 'm1'
        
# --------------------------------
#   Метод учета тика
#   Формат тика: { 'year': , 'month': , 'day': , 'hour': ,
#             'min': , 'sec': , 'bid': , 'ask': }
    def put(self,tick):

        time1 = ttime(tick['year'],tick['month'],tick['day'],tick['hour'],tick['min'],tick['sec'])
        if(self.btime == None):
#           это старт формирования первой свечи
            cndl = candle('m1')
            self.candles.append(cndl)
#           начальное время графика            
            self.btime = time1
            self.current = time1.minute
        if(self.current == time1.minute):
            cndl = self.candles[0]
            cndl.add(tick)
        else:
#           завершение предыдущей свечи
            length = len(self.candles)
            if(length > 0):
                cndl = self.candles[0]
                cndl.complete()
#           начало формирования новой свечи
            cndl = candle('m1')
            cndl.add(tick)
            self.add(cndl)
            self.current = time1.minute

#       обновление текущего времени с каждым тиком    
        self.ctime = time1
        
        return