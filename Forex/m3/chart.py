# Класс "График"
class chart():

# --------------------------------
#   Инициализатор
    def __init__(self,type):

        self.low = []
        self.high = []
        self.open = []
        self.close = []
        self.year = []
        self.month = []
        self.day = []
        self.volume = []
        return
    
# --------------------------------
#   Метод добавления свечи
#   Параметр - массив значений
#   id,low,high,open,close,year,month,day,volume
    def add(self,cndl):

        self.low.append(cndl.low)
        self.high.append(cndl.high)
        self.open.append(cndl.open)
        self.close.append(cndl.close)
        self.year.append(cndl.year)
        self.month.append(cndl.month)
        self.day.append(cndl.day)
        self.volume.append(cndl.volume)

        return