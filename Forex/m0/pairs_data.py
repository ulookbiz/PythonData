# Класс "Pairs"
# Содержит необходимую информацию о каждой паре
class pair_data():
    
# --------------------------------
#   Инициализатор
    def __init__(self):
        
#       валютная пара
        self.pair = ["EURUSD","GBPUSD","ETHUSD"]
#       множитель для перевода цены в пипсы        
        self.pip = [100000,100000,100]
        
        return

# --------------------------------
#   Возврат цены в пипсах
    def pipprice(self,pair):

        ind = self.pair.index(pair)
        ret = self.pip[ind]
        
        return ret
