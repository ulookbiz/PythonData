import MetaTrader5 as mt5
from datetime import datetime
import pytz
import pandas as pd

#........................................................
# Класс обработки данных из сети и раздающий их в объекты графиков
class netDataProcessing():
# --------------------------------
#   Инициализатор
    def __init__(self,pair,now = None):

        self.pair = pair
        self.charts = []
        if(now == None):
            self.now = datetime.now()
        else:
            self.now = now
        self.timezone = pytz.timezone("Etc/UTC")
 
        return

# --------------------------------
#   Метод добавления графика-контейнера свеч
    def chart_add(self,chart):

        self.charts.append(chart)
        
        return

# --------------------------------
#   Метод распределения работы
    def do(self):
                
        for chart in self.charts:
            if(chart.timef == 'd1'):
               self.do_d1(chart)
            elif(chart.timef == 'h1' or chart.timef == 'h4'):
                self.do_h1_h4(chart)
            elif(chart.timef == 'm1' or chart.timef == 'm5' or
                 chart.timef == 'm15' or chart.timef == 'm30'):
                self.do_m1_m5_m15_m30(chart)
                
        return
    
# --------------------------------
#   Метод дополнения графика d1 
    def do_d1(self,chart):

#       количество недостающих свечей
        q = chart.quantity
        
        year = self.now.year
        month = self.now.month
        day = self.now.day
        utc_from = datetime(year, month, day, tzinfo=self.timezone)
        
#       3 стандартные строки создания выходного массива
        rates = mt5.copy_rates_from(self.pair, chart.timeframe, utc_from, q)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
        
        length = len(rates_frame["open"])
        for i in range(0,length):

            cndl = []
            cndl.append(0)
            cndl.append(round(rates_frame["low"][i],5))
            cndl.append(round(rates_frame["high"][i],5))
            cndl.append(round(rates_frame["open"][i],5))
            cndl.append(round(rates_frame["close"][i],5))
            cndl.append(rates_frame["time"].dt.year[i])
            cndl.append(rates_frame["time"].dt.month[i])
            cndl.append(rates_frame["time"].dt.day[i])
            cndl.append(rates_frame["tick_volume"][i])
            cndl.append(rates_frame["spread"][i])     
            chart.candleAdd(cndl)

#        raise SystemExit
        
        return

# --------------------------------
#   Метод дополнения графика h4
    def do_h1_h4(self,chart):
        
#       количество недостающих свечей
        q = chart.quantity
        
        year = self.now.year
        month = self.now.month
        day = self.now.day
        hour = self.now.hour
        utc_from = datetime(year, month, day, hour, tzinfo=self.timezone)

#       3 стандартные строки создания выходного массива
        rates = mt5.copy_rates_from(self.pair, chart.timeframe, utc_from, q)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

        length = len(rates_frame["open"])
        for i in range(0,length):
            cndl = []
            cndl.append(0)
            cndl.append(round(rates_frame["low"][i],5))
            cndl.append(round(rates_frame["high"][i],5))
            cndl.append(round(rates_frame["open"][i],5))
            cndl.append(round(rates_frame["close"][i],5))
            cndl.append(rates_frame["time"].dt.year[i])
            cndl.append(rates_frame["time"].dt.month[i])
            cndl.append(rates_frame["time"].dt.day[i])
            cndl.append(rates_frame["time"].dt.hour[i])
            cndl.append(rates_frame["tick_volume"][i])
            cndl.append(rates_frame["spread"][i])
            
            chart.candleAdd(cndl)

        return

# --------------------------------
#   Метод дополнения графика m1 
    def do_m1_m5_m15_m30(self,chart):

#       количество недостающих свечей
        q = chart.quantity
        
        year = self.now.year
        month = self.now.month
        day = self.now.day
        hour = self.now.hour
        minute = self.now.minute
        utc_from = datetime(year, month, day, hour, minute, tzinfo=self.timezone)

#       3 стандартные строки создания выходного массива
        rates = mt5.copy_rates_from(self.pair, chart.timeframe, utc_from, q)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
        
        length = len(rates_frame["open"])
        for i in range(0,length):

            cndl = []
            cndl.append(0)
            cndl.append(round(rates_frame["low"][i],5))
            cndl.append(round(rates_frame["high"][i],5))
            cndl.append(round(rates_frame["open"][i],5))
            cndl.append(round(rates_frame["close"][i],5))
            cndl.append(rates_frame["time"].dt.year[i])
            cndl.append(rates_frame["time"].dt.month[i])
            cndl.append(rates_frame["time"].dt.day[i])
            cndl.append(rates_frame["time"].dt.hour[i])
            cndl.append(rates_frame["time"].dt.minute[i])
            cndl.append(rates_frame["tick_volume"][i])
            cndl.append(rates_frame["spread"][i])     
            chart.candleAdd(cndl)
        
        return