import winsound
#........................................................
# Класс контроля ситуаций трейдинга
# - достижение ценой определенного уровня
class check():
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.price_level_delete()
        
        return

# --------------------------------
#   Метод добавления контроля уровня цены
    def price_level_add(self,value,move,line):

        self.checked_price = value
        self.move = move
        self.line = line

        print("Запуск контроля",self.pair,":",
        "- достижение отметки", value, "линией",line)
        
        return

# --------------------------------
#   Условия для знаков:
#   "+" - означает "больше или равно"
#   "-" - означает "меньше или равно"
#   Метод удаления контроля уровня цены
    def price_level_delete(self):

        self.checked_price = None
        self.sign = None
        
        return

# --------------------------------
#   Метод выполнения контроля
    def put(self,tick):

        if(self.checked_price == None):
            return
        
        yes1 = False
        if(self.move == '+'):
#           движение вверх
            if(tick[self.line] >= self.checked_price):
                yes1 = True
        else:
#           движение вниз
            if(tick[self.line] <= self.checked_price):
                yes1 = True

#        print(tick[self.line],self.checked_price)

        if(yes1 == True):
            print("Валютная пара:",self.pair,
                  "Достигнут уровень:", self.checked_price)
        if(yes1):
            frequency = 2000
            duration = 100
            winsound.Beep(frequency, duration)
            self.price_level_delete()            
        
        return
