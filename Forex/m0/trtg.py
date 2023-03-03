#....................................
# Класс "toReachTheGoal"
# Проверка достижения требуемого уровня цен для списка пар
#....................................
class toReachTheGoal():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self):

        return

# --------------------------------
#   метод активации контроля цен
#   Формат параметра:
#   dts =
#    [
#      { "pair":"EURUSD", "price":1.3, "direction":"upwards" },
#      { "pair":"GBPUSD", "price":1.3, "direction":"topdown" },
#       ...
#    ]
    def activate(self,dts):

        self.pairs = []
        self.prices = []
        self.dirs = []
        for d in dts:
            self.pairs.append(d['pair'])
            self.prices.append(float(d['price']))
            if(d['direction'] == 'topdown'):
                self.dirs.append(-1)
            else:
                self.dirs.append(1)
        
        return

# --------------------------------
#   метод приема тика с данными
#   Возврат: сообщение или False
    def put(self,pair,tick):

        bid = float(tick['bid'])
        for i in range(len(self.pairs)):
            if(self.pairs[i] == pair):
                answer = self.check(pair,bid,self.prices[i],self.dirs[i])
                if(answer != False):
                    self.pairs[i] = "" # закончить обработки этой порции
                    return answer

        return False

# --------------------------------
#   метод проверки цели и формирования ответа
    def check(self,pair,bid,goal,direction):

        if(direction == 1):
            if(bid >= goal):
                ret = "Достигнута цель цены: "+pair+": "+str(goal)
            else:
                ret = False
        else:
            if(bid <= goal):
                ret = "Достигнута цель цены: "+pair+": "+str(goal)
            else:
                ret = False
        
        return ret
