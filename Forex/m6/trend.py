from funcs import ttime
from pair_ch import pair_ch
from watch import watch
import constant

# Класс "Trend"
# Родительский
class trend():
# --------------------------------
#   Инициализатор
    def __init__(self,pair):
        
        self.pair = pair # текущая пара
        self.bid = None
        self.ask = None
        self.time = None
        self.prev = None
        self.ptime = None
        self.prev2 = None
        self.ptime2 = None
        self.base_bid = None
        self.base_time = None
        self.pc = pair_ch(pair) # параметры пары
        self.sell0 = None
        self.buy0 = None
        self.wtch = watch(300)
        self.maxprofit = 0
        self.profit_time = 0
        
        return

# --------------------------------
#   Метод обработки тика
    def put(self,tick):
        
        if(self.bid == tick['bid']):
            return constant.NOACTION

#       обновление 3-х последних групп данных 
        self.prev2 = self.prev
        self.prev = self.bid
        self.bid = tick['bid']
        self.ask = tick['ask']
        self.ptime2 = self.ptime
        self.ptime = self.time
        self.time = ttime(tick['year'],tick['month'],tick['day'],tick['hour'],tick['min'],tick['sec'])

#       первпя установка точки отсчета
        if(self.base_bid == None):
            self.base_bid = self.bid
            self.base_time = self.time
            return constant.NOACTION

        return self.check(tick) # главный вызов

# --------------------------------
#   Метод подсчета промежутка времени в секундах
    def duration(self):

        duration = self.time-self.base_time
        ret = round(duration.total_seconds())

        return ret

#=========================================================
# Класс "uptrend"
# Поиск лонгового тренда
class uptrend(trend):
# --------------------------------
#   Инициализатор
    def __init__(self,pair):
        
        super().__init__(pair)
        
        return

# --------------------------------
# Метод контроля тренда
    def check(self,tick):

        if(self.buy0 != None):
#           идет процесс покупки            
            ret = self.buy()
            return ret
        
        ret = constant.NOACTION
        if(self.base_bid > self.bid):
#           понижение базовой точки
            self.base_bid = self.bid
            self.base_time = self.time
            return ret
            
        change = round((self.bid - self.base_bid)*self.pc.mult)
        dt = self.duration()
        ph = 0
        if(dt > 0):
            ph = round(change*3600/dt)

#       проверка двух критериев открытия BUY
        if(dt > self.pc.speed['duration'] and ph > self.pc.speed['pips']):
#           открыть покупку            
            ret = self.buy(tick)
        else:
            if(dt > self.pc.speed['drop']):
#               медленная скорость, обновление базовой точки
                self.base_bid = self.bid
                self.base_time = self.time

        return ret

# --------------------------------
# Метод выполнения покупки
    def buy(self,tick):

        ret = constant.BUY_OPEN
        if(self.buy0 == None):
#           открытие покупки            
            self.buy0 = tick['bid']
            self.base_bid = self.buy0            
            self.base_time = self.time
            print("Цена покупки:",self.buy0)
            self.maxprofit = 0
        else:
#           продолжение процесса покупки
            duration = self.time-self.base_time
            dt = round(duration.total_seconds())
            res = round((tick['bid']-self.buy0)*self.pc.mult)
            if(res < 0):
#               процесс в минусе
                if(-res >= self.pc.speed['drawdown']):
#                   допустимая просадка превышена
#                   закрыть покупку с убытком
                    return constant.BUY_CLOSE
                else:
                    pass
            else:
#               процесс в плюсе
                if(res >= self.maxprofit):
#                   процесс набора профита
                    self.maxprofit = res
                    self.profit_time = self.time
                else:
#                   профит уменьшился
                    if((self.maxprofit - res)*10 > self.maxprofit):
#                       потеряно больше 10% макс. профита
#                       учет критерия времени
                        dt = self.duration()
                        if(dt >= self.pc.speed['ddown_time']):
#                           прошло достаточно времени, завершить покупку
                            return constant.BUY_CLOSE
                        else:
#                           прошло мало времени
                            pass
                    else:
                        pass                        
        return ret

#=========================================================    
# Класс "downtrend"
# Поиск шортового тренда
class downtrend(trend):
# --------------------------------
#   Инициализатор
    def __init__(self,pair):
        
        super().__init__(pair)
        return

# --------------------------------
# Метод проверки тренда
    def check(self,tick):

        ret = constant.NOACTION        
        if(self.base_bid < self.bid):
#           понижение базовой точки
            self.base_bid = self.bid
            self.base_time = self.time
            return ret
        
        if(self.sell0 == True):
#           идет процесс продажи
            ret = self.sell()
            return ret
        
        change = round((self.base_bid - self.bid)*self.pc.mult)
        duration = self.time-self.base_time
        dt = round(duration.total_seconds())
        ph = 0
        if(dt > 0):
            ph = round(change*3600/dt)

#       проверка двух критериев открытия SELL
        if(dt > self.pc.speed['duration'] and ph > self.pc.speed['pips']):
            self.sell0 = True
            ret = constant.SELL_OPEN
            self.base_bid = self.bid
            self.base_time = self.time
        else:
            if(dt > self.pc.speed['drop']):
#               обновление базовой точки
                self.base_bid = self.bid
                self.base_time = self.time
        
        return ret

# --------------------------------
# Метод выполнения продажи
    def sell(self,tick):

        ret = constant.SELL_OPEN
        if(self.sell0 == None):
            self.sell0 = tick['bid']
            print("Цена продажи:",self.sell0)
            self.wtch.begin(tick)
        else:
            res = round((self.sell0-tick['bid'])*self.pc.mult)
            if(self.wtch.check(tick) == True):
                print("Результат-sell:", tick['hour'],":",tick['min'],res)
            if(res >= 200):
                print("Прибыль 200 пипсов")
                constant.SELL_CLOSE                

        return ret