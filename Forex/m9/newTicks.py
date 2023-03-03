import MetaTrader5 as mt5
from funcs import noll_1, noll_2, noll_h
import datetime
from datetime import timedelta

#........................................................
# Класс обработки тиков в реальном времени и раздающий их
# в объекты графиков
class newTicks():
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.charts = []
        self.cnt = 0
        self.releasedtime = None
#       учитывает особенность конкретного метатрейдера
        self.time_shift = -3
        
#       первый тик, рассылка по объектам-графикам
        self.tick = mt5.symbol_info_tick(self.pair)

        if(self.tick) != None:
            self.tick = noll_1(self.tick)
            self.tick = noll_h(self.tick,self.time_shift)
            self.bid = self.tick['bid']
            self.sec = self.tick['sec']
            self.actualdata = True

#            print(self.tick)
#            raise SystemExit

        else:
            self.actualdata = False
        
        return

# --------------------------------
#   Метод добавления графика-контейнера свеч
    def chart_add(self,chart):

        self.charts.append(chart)
        return

# --------------------------------
#   Метод обработки тиков, вариант по сравнению с методом do()
    def do3(self):

        if(self.actualdata == False):
            return
            
#        t2 = datetime.datetime.now()+timedelta(hours=self.time_shift)
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
                self.cnt = 0
            else:
                self.cnt += 1

        return
