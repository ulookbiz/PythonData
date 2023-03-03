#........................................................
# Класс Watch
#   - обрабатывает данные времени, для формирования периодов
#       - отработки down-торга
#........................................................
from funcs import ttime

class watch():
# --------------------------------
#   Инициализатор
#   Период контроля задается в секундах
    def __init__(self, period):
        
        self.period = period
        self.start = None
        self.last = None
        self.cnt = 1
        
        return

# --------------------------------
#   Метод задания точки отсчета
    def begin(self, tick):
    
        self.start = ttime(tick['year'],tick['month'],tick['day'],
                     tick['hour'],tick['min'],tick['sec'])
        
        return
    
# --------------------------------
#   Метод проверки достижения периода
    def check(self, tick):
    
        self.last = ttime(tick['year'],tick['month'],tick['day'],
                     tick['hour'],tick['min'],tick['sec'])
        duration = self.last-self.start
        sec = round(duration.total_seconds())
        if(sec < self.period*self.cnt):
            ret = False
        else:
            self.cnt += 1
            ret = True
            
        return ret