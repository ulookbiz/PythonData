#........................................................
# Проверка, тестовая, алгоритмов на прошедших торгах
#   Модуль источника сигналов
#   - продолжает логику главного модуля
#   - управляет работой модулей:
#       - поиска up-тренда
#       - поиска down-тренда
#       - отработки up-торга
#       - отработки down-торга
#........................................................
from datetime import timedelta
#from time import sleep
import MetaTrader5 as mt5
from trend import uptrend,downtrend
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
        self.sell_open = None
        self.buy_open = None
        
        return
    
# --------------------------------
#   Метод управления
    def do(self):
 
#       запуск объектов-трендов
        upt = uptrend(self.pair)
        dnt = downtrend(self.pair)
        
#       цикл с шагом прохода по периоду теста
        mins = 0
        dmin = 5
        while True:
            t1 = self.time_from+timedelta(minutes=mins)
            t2 = t1+timedelta(minutes=dmin)
            if(t2 > self.time_to):
                break
            mins += dmin
            
            ticks = mt5.copy_ticks_range(self.pair,t1,t2, mt5.COPY_TICKS_ALL)
            for t in ticks:
                tick = noll_2(t)
                upt.put(tick)
                dnt.put(tick)
#                sleep(0.2)
#            print(t1,t2)
        return
