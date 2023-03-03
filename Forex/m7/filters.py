import const
from pair_ch import pair_ch
# Класс "check"
# проверка ситуаций графика
class check():
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,area,price=None,time=None,extr=None):
        
        self.ar = area
        self.pc = pair_ch(pair)
        
        self.period = None  # фактический предварительный период
        self.time = time # текущее время
        self.price = price # текущая цена
        self.time_open = time # время открытия сделки
        self.price_open = price # цена открытия сделки
        self.extr = extr # объект учета экстремумов
        
        return
    
# --------------------------------
#   Метод определения последнего движения за период времени
    def lastmove(self,period_var):

#       массив последних данных по ценам за период #1
        period = self.pc.candle[period_var]
        mas = self.ar.data(period)
        if(mas != const.ABSENT):
#           положительное значение self.move означает рост цены            
            self.move = mas['dprice']  # изменение цены в пипсах
            self.period = mas['dtime']  # период изменения
            self.time = mas['time'] # текущее время
            self.price = mas['price'] # текущая цена
            ret = const.OK
        else:
            ret = const.FAIL            
        
        return ret

# --------------------------------
#   Метод возврата текущих - цены и времени
    def get(self):
        
        return { "time":self.time,"price":self.price }

# --------------------------------
#   Метод возврата начальной цены, цены и времени закрытия
    def getclose(self):
        
        return { "priceopen":self.price_open,"timeclose":self.time,"priceclose":self.price }





# ....................................
# Класс "filter1"
# Фильтр поиска лонга по скорости роста цены
class filter1(check):
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,area):
        
        super().__init__(pair,area)

        return

# --------------------------------
#   Метод выполнения проверки
    def do(self):
        
        ret = const.NOACTION
        if(self.lastmove('dur1') == const.OK):
            norma = self.pc.candle['p1']
            if(norma <= self.move):
#               есть быстрый рост цены, открытие сделки
                ret = const.BUY_OPEN
                self.price_open = self.price 
                self.time_open = self.time
                
#                self.ar.dump()
#                raise SystemExit
         
        return ret





# ....................................
# Класс "filter2"
# Фильтр поиска шорта по скорости снижения цены
class filter2(check):
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,area):
        
        super().__init__(pair,area)

        return

# --------------------------------
#   Метод выполнения проверки
    def do(self):
        
        ret = const.NOACTION        
        if(self.lastmove('dur1') == const.OK):
            norma = -self.pc.candle['p1']
            if(norma >= self.move):
#               есть быстрое снижение цены, открытие сделки
                ret = const.SELL_OPEN
                self.price_open = self.price 
                self.time_open = self.time
                
        return ret





# ....................................
# Класс "filter3"
# Фильтр поиска выхода из лонга
class filter3(check):
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,area,price,time,extr):
        
        super().__init__(pair,area,price,time,extr)

        return

# --------------------------------
#   Метод выполнения проверки
    def do(self):
        
        ret = const.BUY
        ldata = self.ar.lastdata()
        self.time = ldata['time']
        self.price = ldata['price']
            
        dev = self.extr.edown(self.price,self.time_open)
#       проверка сильного снижения от экстремума
        if(dev['dprice'] >= self.pc.candle['maxDD']):
            ret = const.BUY_CLOSE
        
        return ret





# ....................................
# Класс "filter4"
# Фильтр поиска выхода из шорта
class filter4(check):
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,area,price,time,extr):
        
        super().__init__(pair,area,price,time,extr)

        return

# --------------------------------
#   Метод выполнения проверки
    def do(self):
        
        ret = const.SELL
        ldata = self.ar.lastdata()
        self.time = ldata['time']
        self.price = ldata['price']

        dev = self.extr.eup(self.price,self.time_open)
#       проверка сильного снижения от экстремума
        if(dev['dprice'] >= self.pc.candle['maxDD']):
            ret = const.SELL_CLOSE

        return ret