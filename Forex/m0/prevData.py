import MetaTrader5 as mt5
from datetime import datetime
import pytz
import pandas as pd

#=====================================
# Класс "Data" - родительский класс для классов каждого таймфрейма
# Служит для извлечения прежних котировок для заданной пары
# Входные параметры: валютная пара, окончание периода времени,
# количество предыдущих свечей
class Data():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        self.quan = quantity # количество свечей
        if(now == None):
            self.now = datetime.now()
        else:
            self.now = now
        self.timezone = pytz.timezone("Etc/UTC")
 
        return
    
# --------------------------------
#   Метод
    def get(self,pair):
       
#       3 стандартные строки создания выходного массива
        rates = mt5.copy_rates_from(pair,self.timeframe,
                                    self.utc_from,self.quan)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')
        
        return rates_frame

#=====================================
# Класс "M1data"
class M1data(Data):

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        super().__init__(quantity,now)
        self.timeframe = mt5.TIMEFRAME_M1
        self.utc_from = datetime(self.now.year,self.now.month,self.now.day,
                            self.now.hour,self.now.minute,tzinfo=self.timezone)
       
#=====================================
# Класс "M5data"
class M5data(Data):

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        super().__init__(quantity,now)
        self.timeframe = mt5.TIMEFRAME_M5
        self.utc_from = datetime(self.now.year,self.now.month,self.now.day,
                        self.now.hour,self.now.minute,tzinfo=self.timezone)

#=====================================
# Класс "M15data"
class M15data(Data):

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        super().__init__(quantity,now)
        self.timeframe = mt5.TIMEFRAME_M15
        self.utc_from = datetime(self.now.year,self.now.month,self.now.day,
                        self.now.hour,self.now.minute,tzinfo=self.timezone)

#=====================================
# Класс "M30data"
class M30data(Data):

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        super().__init__(quantity,now)
        self.timeframe = mt5.TIMEFRAME_M30
        self.utc_from = datetime(self.now.year,self.now.month,self.now.day,
                        self.now.hour,self.now.minute,tzinfo=self.timezone)

#=====================================        
# Класс "H1data"
class H1data(Data):

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        super().__init__(quantity,now) 
        self.timeframe = mt5.TIMEFRAME_H1
        self.utc_from = datetime(self.now.year,self.now.month,self.now.day,
                        self.now.hour,tzinfo=self.timezone)
        
#=====================================        
# Класс "H4data"
class H4data(Data):

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        super().__init__(quantity,now)
        self.timeframe = mt5.TIMEFRAME_H4
        self.utc_from = datetime(self.now.year,self.now.month,self.now.day,
                        self.now.hour,tzinfo=self.timezone)

#=====================================        
# Класс "D1data"
class D1data(Data):

# --------------------------------
#   Инициализатор
    def __init__(self,quantity,now = None):

        super().__init__(quantity,now)
        self.timeframe = mt5.TIMEFRAME_D1
        self.utc_from = datetime(self.now.year,self.now.month,self.now.day,
                        tzinfo=self.timezone)
