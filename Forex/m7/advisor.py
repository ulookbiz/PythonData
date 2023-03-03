from filters import filter1,filter2,filter3,filter4
from funcs import ttime
from extremum import extremum
import const

# Класс "Advisor"
# Советник по основным решениям в рынке - продолжение класса trader
# такая организация позволяет вести одновременно покупку и продажу
# в какие-то периоды времени
# Но Advisor может вести торговлю только одной парой
class advisor():
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,area):

        self.pair = pair
        self.area = area
        
#       фильтры
        self.f1 = filter1(pair,area)
        self.f2 = filter2(pair,area)
        self.f3 = None
        self.f4 = None
        self.extr = extremum()
        self.area.insert(self.extr) # внедрение объекта в объект
        self.buy_price = None
        self.buy_time = None
        self.sell_price = None
        self.sell_time = None

#       показывать график
        self.chart = False

        return
    
# --------------------------------
#   Метод принятия решений о торговле
    def trade(self,mode):
 
        if(mode == "buy"):
            ret = self.guid_buy()
            if(ret == const.BUY_OPEN):
                self.f3 = filter3(self.pair,self.area,
                                  self.buy_price,self.buy_time,
                                  self.extr)
        else:
            ret = self.guid_sell()
            if(ret == const.SELL_OPEN):
                self.f4 = filter4(self.pair,self.area,
                                  self.sell_price,self.sell_time,
                                  self.extr)

        return ret

# --------------------------------
#   Метод принятия решений о покупке
    def guid_buy(self):

        res = self.f1.do()
        if(res == const.BUY_OPEN):
            ret = self.f1.get()
            self.buy_price = ret['price']
            self.buy_time = ret['time']
#.................................................                
#            time0 = self.buy_time-timedelta(hours=3)
            time0 = self.buy_time
            print("Покупка: ",self.buy_price,
              "Время: ",time0.day,
              "-",time0.hour,
              ":",time0.minute,
              ".",time0.second
             )
            self.extr.e_new(self.buy_price,time0,"up")
#            if(self.chart == True):
#                t = time0
#                t = ttime(t.year,t.month,t.day,t.hour,t.minute,0)
#                raise SystemExit
#.................................................

        return res

# --------------------------------
#   Метод принятия решений о продаже
    def guid_sell(self):

        res = self.f2.do()
        if(res == const.SELL_OPEN):
            ret = self.f2.get()
            self.sell_price = ret['price']
            self.sell_time = ret['time']
#.................................................                
#            time0 = self.sell_time-timedelta(hours=3)
            time0 = self.sell_time
            print("Продажа: ",self.sell_price,
              "Время: ",time0.day,
              "-",time0.hour,
              ":",time0.minute,
              ".",time0.second
             )
            self.extr.e_new(self.sell_price,time0,"down")
#            if(self.chart == True):
#                t = time0
#                t = ttime(t.year,t.month,t.day,t.hour,t.minute,0)
#                raise SystemExit

        return res

# --------------------------------
#   Метод контроля процесса покупки
    def buying(self):

        res = self.f3.do()
        if(res == const.BUY_CLOSE):
            ret = self.f3.getclose()
            r = ret['priceclose']-ret['priceopen']
            time = ret['timeclose']
            print("Закрытие покупки: доход=",r,
                  "Цена: ",ret['priceclose'],
                  "Время: ",time.day,
                      "-",time.hour,
                      ":",time.minute,
                      ".",time.second
                 )
        
#            print("Данные зкстремума:",self.extr.up,self.extr.uptime)
        
        return res
        
# --------------------------------
#   Метод контроля процесса покупки
    def selling(self):

        res = self.f4.do()
        if(res == const.SELL_CLOSE):
            ret = self.f4.getclose()
            r = ret['priceopen']-ret['priceclose']
            time = ret['timeclose']
            print("Закрытие продажи: доход=",r,
                  "Цена: ",ret['priceclose'],
                  "Время: ",time.day,
                      "-",time.hour,
                      ":",time.minute,
                      ".",time.second
                 )
        
#            print("Данные зкстремума:",self.extr.down,self.extr.downtime)
            
        return res
