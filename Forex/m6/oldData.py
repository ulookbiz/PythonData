from datetime import datetime, timedelta
import pandas as pd
import pytz
import MetaTrader5 as mt5
import calendar
from funcs import noll_2, period

#........................................................
# Класс, подающий тики прошедшего месяца
class oldDataProcessing():

# --------------------------------
#   Инициализатор
    def __init__(self,pair,timeframe,year,month):

        self.pair = pair
        self.timeframe = timeframe
        if(timeframe == 'h1'):
            self.tf = mt5.TIMEFRAME_H1
        elif(timeframe == 'd1'):
            self.tf = mt5.TIMEFRAME_D1    
        self.year = year
        self.month = month
        
#       текущий день для учета в минутном графике
        self.current_day = 1
        self.last_day = calendar.monthrange(year,month)[1]
        now = datetime.now()
        if(year == now.year and month == now.month):
            self.last_day = now.day
        
        self.timezone = pytz.timezone("Etc/UTC")
        
        return

#--------------------------------
#   Метод обработки данных для таймфреймов d1 и h1
    def result(self):

#       дата окончания периода, количество дней в месяце
        m = self.month + 1
        y = self.year
        d = 1
        if(m == 13):
            m = 1
            y += 1
#       количество дневных свечей
        q = calendar.monthrange(self.year, m)[1] - 6 # минимум 8 выходных
        if(self.timeframe == "h1"):
#           количество часовых свечей 
            q *= 24
    
        utc_from = datetime(y, m, d, tzinfo=self.timezone)
        rates = mt5.copy_rates_from(self.pair, self.tf, utc_from, q)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

        res = []
        for i in range(0,len(rates_frame)):
            if(self.month != rates_frame.time[i].month):
#               выход за пределы месячного диапазона
                continue
            app_to_res = { 
                  "open": round(rates_frame.open[i],5),
                  "high": round(rates_frame.high[i],5),
                  "low": round(rates_frame.low[i],5),
                  "close": round(rates_frame.close[i],5),
                  "volume": rates_frame.tick_volume[i].item(),
                  "spread": rates_frame.spread[i].item(),
                  "day":rates_frame.time[i].day 
                }
            if(self.timeframe != "d1"):
                app_to_res["hour"] = rates_frame.time[i].hour
            res.append(app_to_res)
            
        return res

#--------------------------------
#   Метод обработки данных для таймфрейма m1
#   выполняется проход за 1 день при каждом вызове
    def result2(self):

        if(self.current_day > self.last_day):
#           достигнут конец месяца
            return "End"
        
        day = datetime(self.year, self.month, self.current_day, tzinfo=self.timezone)
        wd = day.weekday()
        if(wd > 4):
#           пропускаем выходные
            day += timedelta(days=7-wd)
               
        if(day.month != self.month):
#           достигнут конец месяца
            return "End"

#       можно извлекать данные
        self.current_day = day.day
        ret = self.ticks()
        self.current_day += 1
                    
        return ret
    
#--------------------------------
#   Метод однодневного прохода для result2
    def ticks(self):
        
        t1 = datetime(self.year, self.month, self.current_day, tzinfo=self.timezone)
        t2 = t1+timedelta(days=1)
        ticks = mt5.copy_ticks_range(self.pair, t1, t2, mt5.COPY_TICKS_ALL)
        if(len(ticks) == 0):
            return None
        
        res = []
        t = noll_2(ticks[0])
        cmin = t['min']
        cbid = t['bid']

        if(cbid < 10):
            mult = 100000
        elif(cbid < 100):
            mult = 10000
        elif(cbid < 1000):
            mult = 1000
        elif(cbid < 10000):
            mult = 100
        else:
            mult = 10

#       начальные значения
        cres = self.res_fill(t,mult)
            
        cnt = 0
        for tick in ticks:
            t = noll_2(tick)
            bid = t['bid']
            if(t['min'] != cmin):
                cres['volume'] = cnt
                res.append(cres)
                cres = self.res_fill(t,mult)
                cnt = 0
                cbid = bid
                cmin = t['min']
            else:
                if(cbid != bid):
                    cres['close'] = bid
                    if(bid > cres['high']):
                        cres['high'] = bid
                    if(bid < cres['low']):
                        cres['low'] = bid
                    cbid = bid
                cres['hour'] = t['hour']
                cnt += 1
#       последняя минута дня
        cres['volume'] = cnt
        res.append(cres)

        for r in res:
            pass
#            print(r['hour'],r['min'], r['open'], r['close'])
#        raise SystemExit        
        return res
    
#--------------------------------
#   Метод вспомогательный
    def res_fill(self, t, mult):
        
        cres = {}
        bid = t['bid']
        cres['open'] = bid
        cres['close'] = bid
        cres['high'] = bid
        cres['low'] = bid
        cres['volume'] = 0
        cres['spread'] = round((t['ask']-bid)*mult)
        cres['day'] = self.current_day
        cres['hour'] = t['hour']
        cres['min'] = t['min']

        return cres