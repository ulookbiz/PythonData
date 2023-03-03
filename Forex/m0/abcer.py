from funcs import ttime,duration
from pairs_data import pair_data
#....................................
# Класс "ABCer"
# отслеживание фигур ABC по тикам
#....................................
class ABCer():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,pairs):

        self.abcs = dict()
        for pair in pairs:
            self.abcs[pair] = abc(pair)

# --------------------------------
#   метод приема тика с данными
    def put(self,pair,tick):

        self.abcs[pair].put(tick)

# --------------------------------
#   метод выполнения обобщения
    def generalization(self,pair):

        print("ABCer: generalization")        
        pass

#=========================================
# Класс abc
class abc():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None

# --------------------------------
#   метод приема тика с данными
    def put(self,tick):

#       разнесение логики по участкам
        if(self.p1 == None):
            self.p1 = Point(tick)
            
        elif(self.p2 == None):
            self.p2 = Point(tick)
            if(self.p2.price == self.p1.price):
                self.p2 = None
            
        elif(self.p4 == None):
            if(self.p3 == None):
                self.put2(tick)
            else:
                self.put3(tick)
        else:
            self.put4(tick)
        
        return

# --------------------------------
#   метод продолжения приема тика с данными "put2"
#   вариант, когда есть 2 точки
    def put2(self,tick):

        v = Vector(self.pair)
        v.calc(self.p1,self.p2)
        if(v.direction == 1):
            if(tick['bid'] >= self.p2.price):
#               обновление 2-й точки
                self.p2 = Point(tick)
            elif(tick['bid'] < self.p2.price):
                if(tick['bid'] > self.p1.price):
#                   создание 3-й точки
                    self.p3 = Point(tick)
                else:
#                   перенос 2-х точек вперед
                    self.p1 = self.p2
                    self.p2 = Point(tick)
        else:
            if(tick['bid'] <= self.p2.price):
#               обновление 2-й точки
                self.p2 = Point(tick)
            elif(tick['bid'] > self.p2.price):
                if(tick['bid'] < self.p1.price):
#                   создание 3-й точки
                    self.p3 = Point(tick)
                else:
#                   перенос 2-х точек вперед
                    self.p1 = self.p2
                    self.p2 = Point(tick)
        return

# --------------------------------
#   метод продолжения приема тика с данными "put3"
#   вариант, когда есть 3 точки
    def put3(self,tick):

        v = Vector(self.pair)
        v.calc(self.p2,self.p3)

        if(v.direction == 1):
            if(tick['bid'] > self.p2.price):
#               продолжение 2-го вектора
                if(tick['bid'] < self.p1.price):
#                   замена 3-й точки
                    self.p3 = Point(tick)
                else:
#                   переход к 2-м точкам
                    self.p1 = self.p2
                    self.p2 = Point(tick)
            else:
#               разворот 2-го вектора
                if(tick['bid'] > self.p2.price):
#                   создание 4-й точки
                    self.p4 = Point(tick)
                else:
#                   переход к 2-м точкам
                    self.p2 = Point(tick)
                    self.p3 = None

        else:
            if(tick['bid'] < self.p2.price):
#               продолжение 2-го вектора
                if(tick['bid'] > self.p1.price):
#                   замена 3-й точки
                    self.p3 = Point(tick)
                else:
#                   переход к 2-м точкам
                    self.p1 = self.p2
                    self.p2 = Point(tick)

            else:
#               разворот 2-го вектора
                if(tick['bid'] < self.p2.price):
#                   создание 4-й точки
                    self.p4 = Point(tick)
                else:
#                   переход к 2-м точкам
                    self.p2 = Point(tick)
                    self.p3 = None
        return

# --------------------------------
#   метод продолжения приема тика с данными "put4"
    def put4(self,tick):

        v = Vector(self.pair)
        v.calc(self.p3,self.p4)
        if(v.direction == 1):
            if(tick['bid'] >= self.p2.price):
#               переход к 2-м точкам
                self.p2 = Point(tick)
            elif(tick['bid'] <= self.p3.price):
#               переход к 3-м точкам
                self.p3 = Point(tick)
                self.p4 = None
            else:
#               обновление 4-й точки
                self.p4 = Point(tick)
        else:
            if(tick['bid'] <= self.p2.price):
#               переход к 2-м точкам
                self.p2 = Point(tick)
            elif(tick['bid'] >= self.p3.price):
#               переход к 3-м точкам
                self.p3 = Point(tick)
                self.p4 = None
            else:
#               обновление 4-й точки
                self.p4 = Point(tick)
        return




#=========================================
# Класс "Point"
# содержит координату "время" и координату "цена"
#....................................
class Point():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,tick):
        
        self.time = ttime(tick['year'],tick['month'],tick['day'],tick['hour'],tick['min'],0)
        self.price = tick['bid']

        return



#=========================================
# Класс "Vector"
#....................................
class Vector():
    pass

# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.distance = None # длина
        self.direction = None # направление (+1, -1)
        self.time = None # время в секундах
        self.speed = None # скорость в "пипсов за час"
        data = pair_data(pair)
        self.pip = data.pip # множитель перевода цены в пипсы

        return

# --------------------------------
#   метод определения вектора
    def calc(self,p1,p2):

        self.distance = round((p2.price - p1.price)*self.pip)
        self.direction = 1
        if(self.distance < 0):
            self.direction = -1
            self.distance = -self.distance
        dur = duration(p1.time,p2.time)
        if(dur > 0):
            self.speed = round(self.distance/dur*3600)        
                
        return
