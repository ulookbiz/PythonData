import MetaTrader5 as mt5
from funcs import noll_2,ttime

#........................................................
# Класс обработки тиков прошедшего времени и раздающий их
# в объекты графиков
from ticks import ticks

class oldTicks(ticks):
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.charts = []
        self.year = None
        self.month = None
        self.tday = None
        self.thour = None
        self.tminute = None

        return

# --------------------------------
#   Метод добавления графика-контейнера свеч
    def chart_add(self,chart):

        self.charts.append(chart)
        return

# --------------------------------
#   Метод установки начальных ограничений времени на формирование графиков
#   Параметры - моменты времени начала формирования свечей
    def limit(self,td,th,tmi):

        self.tday = td
        self.thour = th
        self.tminute = tmi

        return

# --------------------------------
#   Метод обработки тиков из архива
    def do(self,t1,t2):

        bid = sec = None
        cnt = 0        
        ticks = mt5.copy_ticks_range(self.pair, t1, t2, mt5.COPY_TICKS_ALL)

        if(len(ticks) == 0):
            return

        for t in ticks:
            tick = noll_2(t)
            cnt += 1            
#           отработка счетчиков
            if(tick['bid'] != bid or tick['sec'] != sec):
                tkrit = ttime(tick['year'],tick['month'],tick['day'],tick['hour'],tick['min'],tick['sec'])
                tick["volume"] = cnt
                bid = tick['bid']
                sec = tick['sec']
                self.charts[0].put(tick,cnt)
                if(tkrit >= self.thour):
                    self.charts[1].put(tick,cnt)
                    if(tkrit >= self.tminute):
                        self.charts[2].put(tick,cnt)
                cnt = 0

        return