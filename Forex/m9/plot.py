import pandas as pd
import mplfinance as mpf

#........................................................
# Класс построения графика
class plot():
# --------------------------------
#   Инициализатор
    def __init__(self):

        self.times = []
        self.open = []
        self.close = []
        self.high = []
        self.low = []
        self.volume = []

        return

# --------------------------------
#   Метод приема данных времени
    def time_put(self,year,month,day,hour,minute):

        self.times.append(str(year)+"-"+str(month)+"-"+str(day)+
                          " "+str(hour)+":"+str(minute))
        return

# --------------------------------
#   Метод приема данных торговли
    def trade_put(self,open0,close,high,low,volume):

        self.open.append(open0)
        self.close.append(close)
        self.high.append(high)
        self.low.append(low)
        self.volume.append(volume)

        return

# --------------------------------
#   Метод отрисовки
    def plot(self):

        i_array = pd.DatetimeIndex(data=self.times)
        d_array = { "open":self.open,"close":self.close,"high":self.high,"low":self.low,"volume":self.volume }
        df = pd.DataFrame(data=d_array,index=i_array)
        mpf.plot(df,type='candle',volume=False)

        return


#========================================
#a = plot()
#a.time_put(2021,4,1,0,1,0)
#a.time_put(2021,4,1,0,2,0)
#a.time_put(2021,4,1,0,3,0)
#a.time_put(2021,4,1,0,4,0)
#a.trade_put(1,2,3,0,1)
#a.trade_put(2,3,4,1,2)
#a.trade_put(3,5,5,3,1)
#a.trade_put(4,3,7,2,3)
#a.plot()