import numpy as np
#........................................................
# Класс формализации массива чисел в виде паттерна
class pattern():
# --------------------------------
#   Инициализатор
    def __init__(self):

        self.clear()
#        self.real = []
#        self.patt = []

        return

# --------------------------------
#   Метод добавления числа в массив данных
    def add(self,value):

        self.real = np.append(self.real,value)
        self.q += 1
        
        return

# --------------------------------
#   Метод очистки данных
    def clear(self):

#        self.patt = np.array([])
        self.real = np.array([])
        self.q = 0
        
        return

# --------------------------------
#   Метод формирования изоморфной структуры
    def iso(self):

#       отсечение бессмысленных вариантов
        if(self.q < 2):
            return np.array([])

        patt = np.array([0]) # образ массива    
        temp = np.array([self.real[0]]) # истинный массив
        for i in range(1,self.q):
            tmp = self.real[i]  # элемент для добавления
            a = np.where(temp == tmp)[0] # есть в массиве?
            if(len(a) > 0):
                a = a[0]    # индекс
                patt = np.append(patt,patt[a])
                temp = np.append(temp,tmp)
            else:
#               добавление несовпавшего элемента
                length = len(temp)  # длина имеющегося массива
                maxval = 0
                for j in range(length):
                    if(tmp > temp[j]):
                        maxval = max(maxval,patt[j]+1)
                    else:
                        patt[j] += 1
                patt = np.append(patt,maxval)
                temp = np.append(temp,tmp)
#        print(temp)
#        print(patt)

        return patt



#pat = pattern()
#pat.add(1.712)
#pat.add(1.7)
#pat.add(1.713)
#pat.add(1.7)
#pat.add(1.69)
#pat.add(1.695)
#pat.add(1.75)
#pat.add(1.895)
#pat.add(0.75)
#pat.iso(9)