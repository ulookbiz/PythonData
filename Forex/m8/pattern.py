import numpy as np
#........................................................
# Класс формализации массива чисел в виде паттернов
class pattern():
# --------------------------------
#   Инициализатор
    def __init__(self):

        self.real = np.array([],dtype=float) # массив реальных чисел
        self.patt = [] # массив массивов 
        self.elem = np.array([],dtype=int) # основа изо-массивов 

        return

# --------------------------------
#   Метод добавления числа в массив данных
    def add(self,value):

#       начало заполнения массивов
        if(len(self.elem) == 0):
            self.elem = np.append(self.elem,0)
            self.real = np.append(self.real,value)

#       занесение в массив массивов patt
        else:
            self.elem = self.adjust(value) # обновленный elem
            self.real = np.append(self.real,value)
            self.patt.append(self.elem)            
            
#        print(self.real)
#        l = len(self.patt)-1
#        if(l >=0 ):
#            print(self.patt[l])
#        print(' ')
        
        return

# --------------------------------
#   Метод обновления данных массива elem после добавления
#   нового значения
    def adjust(self,val):

        arr = np.where(self.real == val)[0]
        if(len(arr) > 0):
            ind = arr[0]
            m = self.elem[ind]
            el = np.append(self.elem,m)
        else:
            length = len(self.elem)
            m = -1
            el = np.array([],dtype=int) # основа изо-массивов 
            for i in range(length):
                if(val < self.real[i]):
                    el = np.append(el,self.elem[i]+1)
                else:
                    el = np.append(el,self.elem[i])
                    m = max(m,self.elem[i]+1)
            m = max(0,m)
            el = np.append(el,m)
        
        return el

# --------------------------------
#   Метод возврата массива, соответствующего количеству элементов
    def get(self,n=0):

        if(n < 2):
            l = len(self.patt)-1
            if(l > 2):
                ret = self.patt[l]
            else:
                ret = None
        else:
            ret = self.patt[n-2]
        
        return ret


pat = pattern()
pat.add(1.712)
pat.add(1.71)
pat.add(1.713)
pat.add(1.7)
pat.add(1.69)
pat.add(1.695)
pat.add(1.75)
pat.add(1.69)
pat.add(1.713)
pat.add(11)
pat.add(1)

a = pat.get(10)
b = pat.get(10)

print(np.array_equal(a,b))

raise SystemExit