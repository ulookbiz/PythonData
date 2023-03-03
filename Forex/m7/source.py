#........................................................
# Проверка, тестовая, алгоритмов на прошедших торгах
#   Модуль источника данных
#........................................................
import MetaTrader5 as mt5
#from time import sleep
from funcs import noll_2

# Класс "Source"
# Служит источником информации из рынка
class source():
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,time1,time2):
        
        self.pair = pair
        self.time_from = time1
        self.time_to = time2
        self.ticks = mt5.copy_ticks_range(self.pair,time1,time2, mt5.COPY_TICKS_ALL)
        self.cnt = -1
        if self.ticks is None:
            self.length = 0
        else:
            self.length = len(self.ticks)

        return
    
# --------------------------------
#   Метод возврата порции данных
    def get(self,par):

        self.cnt += 1        
        if(self.cnt == self.length):
            return None

        ret = noll_2(self.ticks[self.cnt])
        return ret