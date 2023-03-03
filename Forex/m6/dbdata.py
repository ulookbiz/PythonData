import datetime
from datetime import timedelta
from dbase import dbase
from funcs import ttime

#........................................................
# Класс обработки данных из базы и раздающий их в объекты графиков
class dbDataProcessing():
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.charts = []
        self.now = datetime.datetime.now()
        self.dbase = dbase(pair,self.now.year,self.now.year)
        
        return
    
# --------------------------------
#   Метод добавления графика-контейнера свеч
    def chart_add(self,chart,chart_width):

        self.charts.append(chart)
        self.quantity = chart_width
        
        return
    
# --------------------------------
#   Метод заполнения графиков из базы данных
    def do(self):
                
        for chart in self.charts:
            if(chart.timef == 'd1'):
               self.do_d1(chart)
            elif(chart.timef == 'h1'):
                self.do_h1(chart)
            elif(chart.timef == 'm1'):
                self.do_m1(chart)
                
        return

# --------------------------------
#   Метод заполнения графика D1 из базы данных
    def do_d1(self,chart):

#       настройка окончательной даты расчета с учетом выходных
        t1 = self.now
        if(t1.weekday() == 6):
            t1 = t1-timedelta(days=1)
#       число рабочих дней плюс 5 запаса, идем назад
        q = round(self.quantity*7/5)+5
        t1 = t1-timedelta(days=q)
        
        year = t1.year
        month = t1.month
        self.dbase.setperiod(year,month)
        for i in range(0,q):
            cndl = self.dget(t1)
            t1 += timedelta(days=1)
            if(cndl == None):
                continue
            if(t1.month != month):
                month = t1.month
                year = t1.year
                self.dbase.setperiod(year,month)
            chart.candleAdd(cndl)
            
        return
    
# --------------------------------
#   Метод заполнения графика H1 из базы данных
    def do_h1(self,chart):

#       настройка окончательной даты расчета с учетом выходных
        t1 = self.now
        if(t1.weekday() == 6):
            t1 = t1-timedelta(days=2)
        elif(t1.weekday() == 5):
            t1 = t1-timedelta(days=1)
        tt = ttime(t1.year,t1.month,t1.day,23,59,59)
#       берем назад дополнительно 1 час
        q = self.quantity+1
        t1 = tt-timedelta(hours=q)

        year = t1.year
        month = t1.month
        day = t1.day
        self.dbase.setperiod2(year,month,day)
        for i in range(0,self.quantity):
            cndl = self.hget(t1)
            t1 += timedelta(hours=1)
            if(cndl == None):
                continue
            if(t1.day != day):
                day = t1.day
                month = t1.month
                year = t1.year
                self.dbase.setperiod2(year,month,day)
            chart.candleAdd(cndl)

        return
    
# --------------------------------
#   Метод заполнения графика M1 из базы данных
    def do_m1(self,chart):

#       настройка окончательной даты расчета с учетом выходных
        t1 = self.now
        if(t1.weekday() == 6):
            t1 = t1-timedelta(days=2)
        elif(t1.weekday() == 5):
            t1 = t1-timedelta(days=1)
        tt = ttime(t1.year,t1.month,t1.day,23,59,59)
        q = self.quantity+1        
#       берем назад дополнительно 1 минуту
        t1 = tt-timedelta(minutes=q)
        
        year = t1.year
        month = t1.month
        day = t1.day
        hour = t1.hour
        self.dbase.setperiod3(year,month,day,hour)
        for i in range(0,self.quantity):
            cndl = self.mget(t1)
            t1 += timedelta(minutes=1)
            if(cndl == None):
                continue
            if(t1.day != day):
                day = t1.day
                month = t1.month
                year = t1.year
                hour = t1.hour
                self.dbase.setperiod3(year,month,day,hour)
            chart.candleAdd(cndl)
            
        return
    
#.......................................................
#   Метод формирования подстроки условия select данных дневного графика
    def dget(self,t):

        where = "year='"+str(t.year)+"' and month='"+str(t.month)+"' and day='"+str(t.day)+"'"
        rows = self.dbase.days_select(where)
        if(len(rows) > 0):
            return rows[0]
        else:
            return None

#.......................................................
#   Метод формирования подстроки условия select данных часового графика
    def hget(self,t):

        where = "year='"+str(t.year)+"' and month='"+str(t.month)+"' and day='"+str(t.day)+"' and hour='"+str(t.hour)+"'"
        rows = self.dbase.hours_select(where)
        if(len(rows) > 0):
            return rows[0]
        else:
            return None
        
#.......................................................
#   Метод формирования подстроки условия select данных часового графика
    def mget(self,t):

        where = "year='"+str(t.year)+"' and month='"+str(t.month)+"' and day='"+str(t.day)+"' and hour='"+str(t.hour)+"' and mint='"+str(t.minute)+"'"
        rows = self.dbase.mins_select(where)
        if(len(rows) > 0):
            return rows[0]
        else:
            return None