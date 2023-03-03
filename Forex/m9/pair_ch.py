# Класс "pair_ch"
# Содержит необходимую информацию о каждой паре
class pair_ch():
    
# --------------------------------
#   Инициализатор
    def __init__(self,pair):
        
        self.pair = pair
        
        if(self.pair == "EURUSD"):
#           множитель для перевода цены в пипсы
            self.mult = 10000
            self.significant_value = 5 # пипсов
        if(self.pair == "GBPJPY"):
#           множитель для перевода цены в пипсы
            self.mult = 100
            self.significant_value = 5 # пипсов
        if(self.pair == "GBPUSD"):
#           множитель для перевода цены в пипсы
            self.mult = 10000
            self.significant_value = 5 # пипсов
        if(self.pair == "AUDNZD"):
#           множитель для перевода цены в пипсы
            self.mult = 10000
            self.significant_value = 5 # пипсов
        if(self.pair == "ETHUSD"):
#           множитель для перевода цены в пипсы
            self.mult = 100
            self.significant_value = 5 # пипсов

        return
