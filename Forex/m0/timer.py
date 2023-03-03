# Класс "Timer"
#  отслеживает время и подает сигналы в модуль продолжения
from datetime import datetime,timedelta

class Timer():

# --------------------------------
#   Инициализатор
    def __init__(self,work_time):

        now = datetime.now()
        self.close = False
        self.end = now+timedelta(seconds=work_time)
        self.m1 = now.minute
        self.h1 = now.hour
        self.d1 = now.day

        return

# --------------------------------
#   Метод выполнения, главный
    def check(self):

        now = datetime.now()
        if(now > self.end):
            self.close = True
            return False

        m = now.minute
        ret = False
        if(m != self.m1):
            self.m1 = m
            ret = 'm1'
            if(m%5 == 0):
                ret = 'm5'
                if(m%15 == 0):
                    ret = 'm15'
                    if(m%30 == 0):
                        ret = 'm30'
                        h = now.hour
                        if(h != self.h1):
                            self.h1 = h
                            ret = 'h1'
                            if(h%4 == 0):
                                ret = 'h4'
                                d = now.day
                                if(d != self.d1):
                                    self.d1 = d
                                    ret = 'd1'

        return ret
