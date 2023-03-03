import MetaTrader5 as mt5
from funcs import noll_1, noll_2
import datetime
from datetime import timedelta
from scalper import scalper

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
        self.time_shift = 3
        
#       первый тик, рассылка по объектам-графикам
        self.tick = mt5.symbol_info_tick(self.pair)
        
        if(self.tick) != None:
            self.tick = noll_1(self.tick)
            self.bid = self.tick['bid']
            self.sec = self.tick['sec']
            self.actualdata = True
        else:
            self.actualdata = False
        self.scalper = None # Объект "скальпер"
        
        return

# --------------------------------
#   Метод установки объекта "скальпер"
    def scalper_set(self):

        if(self.scalper == None):
            self.scalper = scalper(self.pair)

        return

# --------------------------------
#   Метод добавления графика-контейнера свеч
    def chart_add(self,chart):

        self.charts.append(chart)
        return

# --------------------------------
#   Метод обработки тиков, вариант по сравнению с методом do()
    def do3(self,scalp):

        if(self.actualdata == False):
            return
            
        if(scalp != None):
            self.scalper_set()
        
        t2 = datetime.datetime.now()+timedelta(hours=self.time_shift)
#        t2 = datetime.datetime.now()
        
        if(self.releasedtime == None):
            t1 = t2+timedelta(seconds=-1)
        else:
            t1 = self.releasedtime
            
#        print(t1," ",t2)
#        raise SystemExit
            
        ticks = mt5.copy_ticks_range(self.pair, t1, t2, mt5.COPY_TICKS_ALL)
        self.releasedtime = t2

        for t in ticks:
            self.tick = noll_2(t)
            
#...................
#            print(self.tick)
#            raise SystemExit
#..................
            
            if(self.bid != self.tick['bid']):
                for chart in self.charts:
                    chart.put(self.tick,self.cnt)
                self.bid = self.tick['bid']
                self.cnt = 0
            else:
                self.cnt += 1

            if(self.scalper != None):
                self.scalper.put(self.tick)

        return
