import MetaTrader5 as mt5
#import pytz
from datetime import timedelta,datetime
import pandas as pd
from funcs import ttime
from plot import plot

from funcs import noll_2

#........................................................
# Класс отрисовки группы свеч вокруг заданного момента времени
class around():
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
#        self.timezone = pytz.timezone("Etc/UTC")
        self.plot = plot()
    
        return

# --------------------------------
#   Метод выполнения отрисовки свеч
#   q - количество свеч
    def do_m1(self,time0,q):

        q1 = round(q/2)
        time = time0+timedelta(minutes=q1)
        year = time.year
        month = time.month
        day = time.day
        hour = time.hour
        minute = time.minute

#        utc_from = datetime(year, month, day, hour, minute, tzinfo=self.timezone)
        tfrom = datetime(year, month, day, hour, minute)
        
#        rates = mt5.copy_rates_from(self.pair, mt5.TIMEFRAME_M1, utc_from, q)
        rates = mt5.copy_rates_from(self.pair, mt5.TIMEFRAME_M1, tfrom, q)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')


        length = len(rates_frame["open"])
        for i in range(0,length):

            self.plot.time_put(rates_frame["time"].dt.year[i],
                               rates_frame["time"].dt.month[i],
                               rates_frame["time"].dt.day[i],
                               rates_frame["time"].dt.hour[i],
                               rates_frame["time"].dt.minute[i],
                               0
                              )
            self.plot.trade_put(round(rates_frame["open"][i],5),
                                round(rates_frame["close"][i],5),
                                round(rates_frame["high"][i],5),
                                round(rates_frame["low"][i],5),
                                round(rates_frame["tick_volume"][i],5)
                               )


        self.plot.plot()
        return

# --------------------------------
#   Метод выполнения посекундной отрисовки минуты
    def do_m2(self,time0):

        time1 = time0
        y = time1.year
        m = time1.month
        d = time1.day
        ho = time.hour
        mi = time.minute
        time2 = time0+timedelta(minutes=1)
        ticks = mt5.copy_ticks_range(self.pair,time1,time2, mt5.COPY_TICKS_ALL)
        
        s = -1
        for tick in ticks:
            t = noll_2(tick)
#            print(t)
            if(s == -1):
                s = t['sec']
                o = t['bid']
                c = t['bid']
                h = t['bid']
                l = t['bid']
            else:
                if(s != t['sec']):
                    self.plot.time_put(y,m,d,ho,mi,s)
                    self.plot.trade_put(o,c,h,l,0)
                    s = t['sec']
                    o = t['bid']
                    c = t['bid']
                    h = t['bid']
                    l = t['bid']
                else:           
                    c = t['bid']
                    h = max(t['bid'],h)
                    l = min(t['bid'],l)

        self.plot.time_put(y,m,d,ho,mi,s)
        self.plot.trade_put(o,c,h,l,0)
        self.plot.plot()
                
        return


#===========================================
mt5.initialize()

time = ttime(2021,8,11,18,30,0)
ar = around("EURUSD")
ar.do_m1(time,10)
ar = around("EURUSD")
ar.do_m2(time)

raise SystemExit