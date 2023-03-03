import MetaTrader5 as mt5
from datetime import datetime,timedelta
from funcs import noll_2

#........................................................
# Класс-источник обработки тиков
class ticksSource():
# --------------------------------
#   Инициализатор
    def __init__(self):
        
        return
    
# --------------------------------
#   Метод чтения тика для указанной пары
    def get(self,pair):

        t2 = datetime.now()+timedelta(hours=2) # все-таки 2 часа разницы
        t1 = t2+timedelta(seconds=-5)
            
        ticks = mt5.copy_ticks_range(pair, t1, t2, mt5.COPY_TICKS_ALL)

        if ticks is None:
            tick = None
        else:
            if(len(ticks) > 0):
                tick = ticks[-1]
                tick = noll_2(tick)
            else:
                tick = None
        
        return tick