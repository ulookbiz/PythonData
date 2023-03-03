from collections import deque
from pair_ch import pair_ch
from funcs import ttime, duration
from plot import plot

# Класс "Vector"
# Учет текущего вектора изменения цены
class vector():
# --------------------------------
#   Инициализатор
    def __init__(self,pair,termin):

#   termin - срок в секундах для ведения текущего вектора цены        
        self.termin = termin
#   массив секунд учета, в нем самый свежий индекс = 0
#   массив состоит из очереди смещений в секундах относительно
#   self.time. По сути, self.time - это 0 для этой очереди
        self.seconds = deque()
#   массив цен учета, в нем самый свежий индекс = 0
#   массив цен, параллельный массиву секунд
        self.prices = deque()
#   текущее время
        self.time = None
#   текущая цена в момент self.time
        self.price = None
#   доступ к данным валютной пары
        self.pc = pair_ch(pair)

#   чертеж
        self.plot = plot()

        return

# --------------------------------
#   Метод приема тика
    def put(self,tick):
        
        lprice = round(tick['bid']*self.pc.mult)
        ltime = ttime(tick['year'],tick['month'],tick['day'],tick['hour'],
                      tick['min'],tick['sec'])
        
        if self.time is None:
            self.time = ltime
            self.price = lprice
            return
        
        if(self.time == ltime):
#           время не изменилось
            self.price = lprice
            return
        
#       обновление учетных данных
        dt = duration(self.time,ltime)
        for i,s in enumerate(self.seconds):
            self.seconds[i] = s+dt
        self.time = ltime
        self.seconds.appendleft(dt)

        self.prices.appendleft(self.price)
        self.price = lprice
        
        length = len(self.seconds)
        print(length)
        while(self.seconds[length-1] > self.termin):
            self.seconds.pop()
            self.prices.pop()
            length = len(self.seconds)
            print("l:",length)

#..................................
#        print("dt=",dt)
#        print(tick)
#        print(self.seconds)
#        print(self.prices)
#..................................

        return

# --------------------------------
#   Метод возврата данных текущего вектора
    def vec(self):
        
        lastind = len(self.seconds)-1
        if(lastind < 0):
            return None
        
        vect = self.price-self.prices[lastind]

        return {"dtime":self.seconds[lastind], "value":vect}

# --------------------------------
#   Метод распечатки данных - failed
    def dump(self):

        print("---------------------------------")
        print("VECTOR:")
        print(" ")
        print("seconds:")
        print(self.seconds)        
        print(" ")
        print("prices:")
        print(self.prices)
        print(" ")
        print("time:",self.time)
        print(" ")
        print("price:",self.price)
        print("=================================")
        
#        length = len(self.seconds)
#        for i in range(0,length):
#            s = self.seconds[i]-1
#            p = self.prices[i]
#            self.plot.time_put(2021,3,1,0,s,0)
#            self.plot.trade_put(1,p-118050,p-118050,1,0)
#        self.plot.plot()
        
        return