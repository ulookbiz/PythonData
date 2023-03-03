import const
from pair_ch import pair_ch
from area import area
from advisor import advisor

# Класс "Trader"
# Торгующий класс
class trader():
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair,source):
        
        self.pair = pair
        self.pc = pair_ch(pair)

#       объект - источник данных
        self.src = source
#       объект, содержащий обработанные данные        
        self.ar = area(pair)        
#       объект-советник по принятию решений
        self.adv = advisor(pair,self.ar)
        
        return
    
# --------------------------------
#   Метод управления торговлей
    def do(self):
        
        buy_status = const.NOACTION
        sell_status = const.NOACTION        

        while True:
#           обновление области данных торговли
            tick = self.src.get(self.pc.tick_timeout)
            if(tick == None):
                break
            
            self.ar.put(tick)

#           проверка после каждого тика
#           по покупке
            if(buy_status == const.BUY):
#               идет процесс покупки
                result = self.adv.buying()
                if(result == const.BUY_CLOSE):
                    buy_status = const.NOACTION
            else:
#               проверить возможность покупки
                result = self.adv.trade("buy")
                if(result == const.BUY_OPEN):
                    buy_status = const.BUY

#           по продаже
            if(sell_status == const.SELL):
#               идет процесс продажи
                result = self.adv.selling()                
                if(result == const.SELL_CLOSE):
                    sell_status = const.NOACTION
            else:
#               проверить возможность продажи
                result = self.adv.trade("sell")
                if(result == const.SELL_OPEN):
                    sell_status = const.SELL
                    
#                   отладка
#                    self.ar.dump()
#                    raise SystemExit

        return
