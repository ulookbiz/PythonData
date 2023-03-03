#........................................................
# Прием, обработка тиков и запись результатов в БД
#........................................................

from datetime import datetime, date, time
from datetime import timedelta
from ticksControl import ticks,oldTicks,newTicks
from funcs import ttime

#........................................................
#nt = newTicks("EURUSD")
#nt.do()
#........................................................
year = 2020
month = 1
day = 1
qdays = 367
#.......................................................
d1 = ttime(year,month,day,0,0,0)
for i in range(1,qdays):
    ot = oldTicks("EURUSD")
    ot.mdb = True
    ot.hdb = True
    ot.ddb = True
    ot.tbclear(d1.year,d1.month,d1.day)
    ot.day(d1.year,d1.month,d1.day)
    d1 = d1+timedelta(days=1)
#........................................................