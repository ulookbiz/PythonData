#........................................................
# Чтение данных из БД и отрисовка графиков
#........................................................

import pandas as pd
import mplfinance as mpf
from plots import plot
#........................................................
# Отриcовка части минутного графика
#year = 2021
#month = 3
#day = 2
#hour = 21
#mint = 30
#delta = 60
#pl = plot("EURUSD")
#tmp = pl.mget(year,month,day,hour,mint,delta)
#ind_arr = pl.indarr(tmp,1)
#body_arr = pl.bodyarr(tmp,1)
#........................................................
# Отриcовка части часового графика
#year = 2021
#month = 3
#day = 2
#hour = 2
#delta = 60
#pl = plot("EURUSD")
#tmp = pl.hget(year,month,day,hour,delta)
#print(tmp)
#ind_arr = pl.indarr(tmp,2)
#body_arr = pl.bodyarr(tmp,2)
#........................................................
# Отриcовка части дневного графика
year = 2020
month = 7
day = 1
delta = 60
pl = plot("EURUSD")
tmp = pl.dget(year,month,day,delta)
ind_arr = pl.indarr(tmp,3)
#print(ind_arr)
body_arr = pl.bodyarr(tmp,3)
#print(body_arr)

d_array = pd.DatetimeIndex(data=ind_arr)
df = pd.DataFrame(data=body_arr,index=d_array)
mpf.plot(df,type='candle',volume=True)
