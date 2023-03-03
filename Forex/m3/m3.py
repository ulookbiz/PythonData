#........................................................
# Обработка данных из БД: вычисление среднего размера свечей
#........................................................

import datetime
from datetime import timedelta
from candle import candle
from chart import chart
from funcs import ttime,period
from dbAccess import dbData


#    if date.month == 12:
#        return date.replace(day=31)
#    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)


#........................................................
year = 2020
month = 1
day = 1
h1 = ttime(year,month,1,0,0,0)
if(h1.month == 12):
    qhours = 31
else:
    dt = h1.replace(month=h1.month+1, day=1) - datetime.timedelta(days=1)
    qhours = dt.day
hour = 0
qhours *= 24

#.......................................................
dbd = dbData("EURUSD")  # объект, читающий свечные данные
ch = chart("EURUSD") # объект "график" - набор свечей

h1 = ttime(year,month,1,0,0,0)

for i in range(1,qhours):
    data = dbd.hget(h1.year,h1.month,h1.day,h1.hour)
    if(data):
        cndl = candle("EURUSD") # объект "свеча"
        c = cndl.h1Candle(data)
        ch.add(c)
    h1 = h1+timedelta(hours=1)
    
op = ch.open
cl = ch.close
sum1 = 0
sum2 = 0
cnt = 0
for i in range(1,len(op)):
    r = abs(ch.open[i]-ch.close[i])
    s = abs(ch.high[i]-ch.low[i])
    sum1 += r
    sum2 += s
    cnt += 1

res1 = round(sum1/cnt,5)
res2 = round(sum2/cnt,5)
print(sum1," ",sum2," ",cnt," ",res1," ",res2)
