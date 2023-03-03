from pairs_data import pair_data
#....................................
# Класс "checkspeed"
# Управление контролем скорости изменения цен
# для разных пар
#....................................
class checkspeed():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self):

        self.pd = pair_data()
        
        return

# --------------------------------
#   метод активации контроля цен
#   Формат параметра:
#   dts =
#    [
#      { "pair":"EURUSD },
#      { "pair":"GBPUSD" },
#       ...
#    ]
    def activate(self,dts):

        self.prs = []
        self.objs = []
        for dt in dts:
            obj = spobj(dt,self.pd)
            self.prs.append(dt)
            self.objs.append(obj)

        return

# --------------------------------
#   метод приема тика с данными
    def put(self,pair,tick):

        ind = self.prs.index(pair)
        obj = self.objs[ind]
        obj.put(tick)

        return

# --------------------------------
#   метод отображения текущих скоростей
    def generalization(self,pair,period):

        ind = self.prs.index(pair)
        obj = self.objs[ind]
        crit = period
        while(crit is not None):
            if(crit == 'd1'):
                quan = 60*24
            elif(crit == 'h4'):
                quan = 60*4
            elif(crit == 'h1'):
                quan = 60
            elif(crit == 'm30'):
                quan = 30
            elif(crit == 'm15'):
                quan = 15
            elif(crit == 'm5'):
                quan = 5
            elif(crit == 'm1'):
                quan = 1
            
            ans = obj.calc(quan)
            
#            print(quan,ans)
#            raise SystemExit
            
            if(ans != False):
                tp = ans['period']
                print("Пара:",pair,"Период:",tp,"Скорость:",ans['change'])
#                raise SystemExit
                if(tp > 60*4):
                    crit = 'h4'
                elif(tp > 60):
                    crit = 'h1'
                elif(tp > 30):
                    crit = 'm30'
                elif(tp > 15):
                    crit = 'm15'
                elif(tp > 5):
                    crit = 'm5'
                elif(tp > 1):
                    crit = 'm1'
                else:
                    crit = None                
            else:
                break

        return


#=========================================
#....................................
# Класс "spobj"
# Контроль скорости изменения цен
#....................................
class spobj():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,pair,pd):

        self.pair = pair
        self.pair_data = pd
        self.edge = None
        self.prices = []
        self.lastmin = 0
        self.lastprice = 0.0
        
        return

# --------------------------------
#   метод приема тика с данными
    def put(self,tick):

        if self.edge is None:
#           первый тик учета
            self.edge = {"year":tick['year'],
                         "month":tick['month'],
                         "day":tick['day'],
                         "hour":tick['hour'],
                         "min":tick['min']
                        }
            self.prices.append(tick['bid'])
            self.lastmin = tick['min']
        else:
#           основной учет
            if(self.lastmin != tick['min']):
#               изменения в массивах из-за смены текущей минуты
                self.update(tick)
            self.lastprice = tick['bid']
            
        return False

# --------------------------------
#   вспомогательный метод обновления индекса и массива цен
#   из-за смены текущей минуты
    def update(self,tick):
        
        mint = tick['min']
        m = self.currmin(mint,-1)
        while(m != self.lastmin):
#           занесение цены для пропущенных минут
            self.add(self.lastprice)
            m = self.currmin(mint,-1)
        
        self.add(tick['bid'])
        self.lastmin = mint

        return

# --------------------------------
#   вспомогательный метод расчета текущей минуты
    def currmin(self,cm,change):

        ret = cm+change
        if(ret < 0):
            ret += 60
        elif(ret > 59):
            ret -= 60
        
        return ret

# --------------------------------
#   вспомогательный метод для работы с массивом цен
    def add(self,price):
        
        if(len(self.prices) == 60):
            self.prices.pop(0)
        self.prices.append(price)

        return
    
# --------------------------------
#   подсчет скорости в пипсах за 1 час в течение периода (минут)
#   или меньше, если период пока короче
    def calc(self,period):
    
        leng = len(self.prices)
        if(leng > 1):
            if(period < leng-1):
                change = self.prices[leng-1]-self.prices[leng-period-1]
                rpr = period
            else:
                change = self.prices[leng-1]-self.prices[0]
                rpr = leng-1
            change = round(change*self.pair_data.pipprice(self.pair)/rpr*60)
            ret = {"period":rpr,"change":change}
            
            print("-",self.prices,"==")
        else:
            ret = False
    
        return ret