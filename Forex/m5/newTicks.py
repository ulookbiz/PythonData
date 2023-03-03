import MetaTrader5 as mt5
from funcs import noll_1, noll_2
from time import sleep
import datetime
from datetime import timedelta

#........................................................
# Класс обработки тиков в реальном времени и раздающий их
# в объекты графиков
from ticks import ticks

class newTicks(ticks):
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.charts = []
#       первый тик, рассылка по объектам-графикам
        self.tick = mt5.symbol_info_tick(self.pair)
        self.tick = noll_1(self.tick)
        self.bid = self.tick['bid']
        self.sec = self.tick['sec']
        self.cnt = 0
        self.releasedtime = None


        return

# --------------------------------
#   Метод добавления графика-контейнера свеч
    def chart_add(self,chart):

        self.charts.append(chart)
        return

# --------------------------------
#   Метод циклической обработки поступающих тиков
    def do(self):

#       цикл обработки поступающих тиков
        for chart in self.charts:
            chart.put(self.tick,0)

        count = 10000000 # ограничитель цикла
        cnt = 0 # счетчик пропущенных тиков

        while(count > 0):
            tick = mt5.symbol_info_tick(self.pair)
            count -= 1
            self.tick = noll_1(tick)
            if(self.sec == self.tick['sec'] and self.bid == self.tick['bid']):
                cnt += 1
                continue
            for chart in self.charts:
                chart.put(self.tick,cnt)
            cnt = 0
            self.sec = self.tick['sec']
            self.bid = self.tick['bid']
            sleep(0.5)

        return

# --------------------------------
#   Метод обработки тиков, вариант по сравнению с методом do()
    def do2(self):

#       цикл обработки поступающих тиков
        for chart in self.charts:
            chart.put(self.tick,0)

        cnt = 0 # счетчик пропущенных тиков в течение секунды
#       лимит времени для одного инструмента
        now = datetime.datetime.now()
        limit = now+timedelta(seconds=0.2)

        while(now < limit):
            tick = mt5.symbol_info_tick(self.pair)
            self.tick = noll_1(tick)
            if(self.bid != self.tick['bid']):
#                print(self.pair," ",self.tick['bid']," ",now.second)
                for chart in self.charts:
                    chart.put(self.tick,cnt)
                self.bid = self.tick['bid']
                cnt = 0
            else:
                cnt += 1
            sleep(0.01)
            now = datetime.datetime.now()
            
        return

# --------------------------------
#   Метод обработки тиков, вариант по сравнению с методом do()
    def do3(self):

        t2 = datetime.datetime.now()
        if(self.releasedtime == None):
            t1 = t2+timedelta(seconds=-1)
        else:
            t1 = self.releasedtime
        ticks = mt5.copy_ticks_range(self.pair, t1, t2, mt5.COPY_TICKS_ALL)
        self.releasedtime = t2

        for t in ticks:
            self.tick = noll_2(t)
            if(self.bid != self.tick['bid']):
                for chart in self.charts:
                    chart.put(self.tick,self.cnt)
                self.bid = self.tick['bid']
                print(self.pair," ",self.tick['sec']," ",self.tick['bid']," ",self.cnt)
                self.cnt = 0
            else:
                self.cnt += 1

        return
