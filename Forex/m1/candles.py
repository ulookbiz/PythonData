from candle import M1candle,H1candle 

# Класс работы с коллекцией свеч
class candles():

# ---------------------------------
#   Инициализатор    
    def __init__(self):

        self.list = []
        return

#---------------------------------
#   Метод приема свечи
    def put(self,candle):

        self.list.append(candle)

        try:
            if(candle['hour'] == 23):
                pass
#                print(candle)
        except:
            pass
            #            print(candle)
            
        return

