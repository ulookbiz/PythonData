from funcs import duration
# ....................................
# Класс "extremum"
# Слежение за экстремумами тренда
class extremum():
    
# --------------------------------
#   Инициализатор
    def __init__(self):
        
        self.up = 0
        self.down = 999999
        self.uptime = None
        self.downtime = None
        
        return

# --------------------------------
#   Метод учета порции данных
    def put(self,price,time):

        if(self.up < price):
#           обновление точки отсчета
            self.up = price
            self.uptime = time
        if(self.down > price):
#           обновление точки отсчета
            self.down = price
            self.downtime = time
            
        return

# --------------------------------
#   Метод обновления экстремума (забыть прежний экстремум)
    def e_new(self,price,time,mode):

        if(mode == "up"):
#           обновление точки отсчета
            self.up = price
            self.uptime = time
        else:
#           обновление точки отсчета
            self.down = price
            self.downtime = time

        return
    
# --------------------------------
#   Метод расчета снижения от экстремума
    def edown(self,price,time):

        dp = self.up - price
        if(time > self.uptime):
            dt = duration(self.uptime, time)
        else:
            dt = duration(time, self.uptime)

        return {"dtime":dt,"dprice":dp}

# --------------------------------
#   Метод расчета подъема от экстремума
    def eup(self,price,time):

        dp = price-self.down
        if(time > self.downtime):
            dt = duration(self.downtime, time)
        else:
            dt = duration(time, self.downtime)

        return {"dtime":dt,"dprice":dp}