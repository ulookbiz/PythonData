from collections import deque
from pair_ch import pair_ch
from funcs import ttime, duration
import const

# Класс "Area"
# Область данных торговли в памяти
class area():
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.pc = pair_ch(pair)
        self.extr = None # объект учета экстремумов
        self.volume  = 600 # объем хранения данных в памяти
        self.secs = deque() # массив секунд
        self.val1 = deque() # массив цен параллельно массиву секунд
        self.start_time = None

        return

# --------------------------------
#   Метод внедрения 
    def insert(self,obj):

        self.extr = obj

        return
    
# --------------------------------
#   Метод приема тика
    def put(self,tick):
 
        price = round(tick['bid']*self.pc.mult)
        stime = ttime(tick['year'],tick['month'],tick['day'],tick['hour'],
                      tick['min'],tick['sec'])

#       учет тика в объекте учета экстремумов
        self.extr.put(price,stime)

#       учет тика в массиве секунд
#       массив - "справа-налево", т.е. более поздние данные слева
        length = len(self.secs)
        if(length == 0):
            self.secs.appendleft(stime)
            self.val1.appendleft(price)
            self.start_time = stime
        else:            
            if(stime != self.secs[0]):
#               новые данные
                if(length == self.volume):
#                   требуется сдвиг массива
                    self.secs.pop()
                    self.val1.pop()
                    self.start_time = self.secs[length-2]
                self.secs.appendleft(stime)
                self.val1.appendleft(price)
            else:
#               просто обновление цены
                self.val1[0] = price

        return

# --------------------------------
#   Метод возврата данных за отрезок времени
#   par - количество времени требуемого отрезка
    def data(self,par):

        if(self.start_time == None):
            return const.ABSENT
        
        dt = duration(self.start_time,self.secs[0])
        if(dt < par):
            return const.ABSENT

#       определение индекса() начала отрезка
        i = len(self.secs)-1
        while(i > 0):
            dt = duration(self.secs[i],self.secs[0])
            if(dt > par):
                i-= 1
            else:
                break

#       положительное значение dprice означает рост цены
        dprice = round(self.val1[0]-self.val1[i])
        ret = {"dtime":dt,"time":self.secs[0],"dprice":dprice,
               "price":self.val1[0]}

        return ret
   
# --------------------------------
#   Метод возврата данных после последнего тика
    def lastdata(self):

        ret = {"time":self.secs[0],"price":self.val1[0]}
        return ret

# --------------------------------
#   Метод возврата минимальной и максимальной цены
    def minmax(self):

        ret = {"min":min(self.val1),"max":max(self.val1)}

        return ret




# --------------------------------
#   Метод обновления экстремума при покупке
    def buy_ini(self):

        return

# --------------------------------
#   Метод обновления экстремума при продаже
    def sell_ini(self):

        return

# --------------------------------
#   Метод распечатки данных
    def dump(self):

        print("---------------------------------")
        print("AREA:")
        print(" ")
        print("secs:")
#        for s in self.secs:
#            print(s.hour,s.minute,s.second)
#        print(self.secs)

        for i in range(100):
            print(self.secs[i].hour,
                  self.secs[i].minute,
                  self.secs[i].second,
                  self.val1[i]
                  )
       
        print(" ")
#        print("val1:")
#        print(self.val1)
        print(" ")
        print("start_time:",self.start_time)
        print("=================================")
        
        return
