import MetaTrader5 as mt5
from time import sleep
from datetime import timedelta
import datetime
from funcs import noll_2

pair = "EOSUSD"
mt5.initialize()

for i in range(20):
    t2 = datetime.datetime.now()
    t1 = t2+timedelta(seconds=-0.4)
    ticks = mt5.copy_ticks_range(pair, t1, t2, mt5.COPY_TICKS_ALL)

    for t in ticks:
        tick = noll_2(t)
        print(tick)
    sleep(0.4)