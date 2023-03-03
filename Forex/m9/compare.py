import numpy as np
from pattern import pattern
#........................................................
# Класс выполняющий сравнение частей графиков
class compare():
# --------------------------------
#   Инициализатор
    def __init__(self):

        return

# --------------------------------
#   Метод сравнения графиков по точкам "close"
    def do_close(self,work,sample):

#       количество свечей
        candles_q = len(work.candles)
#       максимальное количество совпадений
        q_max = 0
#       результирующий индекс лучшего совпадения
        result_index = 0
#       внешний цикл по текущему графику
        for start_ind in range(candles_q):
            wpat = pattern()
            spat = pattern()
            j = 0
            for i in range(start_ind,candles_q):
                wpat.add(work.candles[j].close)
                spat.add(sample.candles[i].close)
                if(j > 0):
                    wim = wpat.iso()
                    sim = spat.iso()
                    if(np.array_equal(wim,sim) == False):
                        if(q_max < j):
                            q_max = j
                            result_index = start_ind+j-1
                        break
                j += 1

        return {"q":q_max,"ind":result_index}

# --------------------------------
#   Метод сравнения графиков по точкам "high"
    def do_high(self,work,sample):

#       количество свечей
        candles_q = len(work.candles)
#       максимальное количество совпадений
        q_max = 0
#       результирующий индекс лучшего совпадения
        result_index = 0
#       внешний цикл по текущему графику
        for start_ind in range(candles_q):
            wpat = pattern()
            spat = pattern()
            j = 0
            for i in range(start_ind,candles_q):
                wpat.add(work.candles[j].high)
                spat.add(sample.candles[i].high)
                if(j > 0):
                    wim = wpat.iso()
                    sim = spat.iso()
                    if(np.array_equal(wim,sim) == False):
                        if(q_max < j):
                            q_max = j
                            result_index = start_ind+j-1
                        break
                j += 1

        return {"q":q_max,"ind":result_index}

# --------------------------------
#   Метод сравнения графиков по точкам "low"
    def do_low(self,work,sample):

#       количество свечей
        candles_q = len(work.candles)
#       максимальное количество совпадений
        q_max = 0
#       результирующий индекс лучшего совпадения
        result_index = 0
#       внешний цикл по текущему графику
        for start_ind in range(candles_q):
            wpat = pattern()
            spat = pattern()
            j = 0
            for i in range(start_ind,candles_q):
                wpat.add(work.candles[j].low)
                spat.add(sample.candles[i].low)
                if(j > 0):
                    wim = wpat.iso()
                    sim = spat.iso()
                    if(np.array_equal(wim,sim) == False):
                        if(q_max < j):
                            q_max = j
                            result_index = start_ind+j-1
                        break
                j += 1

        return {"q":q_max,"ind":result_index}

# --------------------------------
#   Метод сравнения графиков по точкам "high" и "low"
    def do_highlow(self,work,sample):

#       количество свечей
        candles_q = len(work.candles)
#       максимальное количество совпадений
        q_max = 0
#       результирующий индекс лучшего совпадения
        result_index = 0
#       внешний цикл по текущему графику
        for start_ind in range(candles_q):
            wpat = pattern()
            spat = pattern()
            j = 0
            for i in range(start_ind,candles_q):
                wpat.add(work.candles[j].high+work.candles[j].low)
                spat.add(sample.candles[i].high+sample.candles[i].low)
                if(j > 0):
                    wim = wpat.iso()
                    sim = spat.iso()
                    if(np.array_equal(wim,sim) == False):
                        if(q_max < j):
                            q_max = j
                            result_index = start_ind+j-1
                        break
                j += 1

        return {"q":q_max,"ind":result_index}

# --------------------------------
#   Метод сравнения графиков по точкам "open" и "high"
    def do_openhigh(self,work,sample):

#       количество свечей
        candles_q = len(work.candles)
#       максимальное количество совпадений
        q_max = 0
#       результирующий индекс лучшего совпадения
        result_index = 0
#       внешний цикл по текущему графику
        for start_ind in range(candles_q):
            wpat = pattern()
            spat = pattern()
            j = 0
            for i in range(start_ind,candles_q):
                wpat.add(work.candles[j].open)
                wpat.add(work.candles[j].high)
                spat.add(sample.candles[i].open)                
                spat.add(sample.candles[i].high)
                if(j > 0):
                    wim = wpat.iso()
                    sim = spat.iso()
                    if(np.array_equal(wim,sim) == False):
                        if(q_max < j):
                            q_max = j
                            result_index = start_ind+j-1
                        break
                j += 1

        return {"q":q_max,"ind":result_index}
    
# --------------------------------
#   Метод сравнения графиков по точкам "open" и "low"
    def do_openlow(self,work,sample):

#       количество свечей
        candles_q = len(work.candles)
#       максимальное количество совпадений
        q_max = 0
#       результирующий индекс лучшего совпадения
        result_index = 0
#       внешний цикл по текущему графику
        for start_ind in range(candles_q):
            wpat = pattern()
            spat = pattern()
            j = 0
            for i in range(start_ind,candles_q):
                wpat.add(work.candles[j].open)
                wpat.add(work.candles[j].low)
                spat.add(sample.candles[i].open)                
                spat.add(sample.candles[i].low)
                if(j > 0):
                    wim = wpat.iso()
                    sim = spat.iso()
                    if(np.array_equal(wim,sim) == False):
                        if(q_max < j):
                            q_max = j
                            result_index = start_ind+j-1
                        break
                j += 1

        return {"q":q_max,"ind":result_index}