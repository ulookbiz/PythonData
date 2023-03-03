from funcs import ttime
import pandas as pd
from datetime import timedelta
from dbase import dbase

#........................................................
# Класс, формирующий данные для построения графика
class plot():
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
        self.dbase = dbase(pair)
        
        return

#.......................................................
#   Метод формирования подстроки условия select данных минутного графика
    def mget(self,year,month,day,hour,mint,delta):

        t2 = ttime(year, month, day, hour, mint, 0)+timedelta(minutes=delta)
        where = ""

        or_condition = False
        if(t2.hour != hour):
#           переход периода через границу часа
            where += "("
            where += self.eq("year",year,False)
            where += self.eq("month",month,True)
            where += self.eq("day",day,True)
            where += self.eq("hour",hour,True)
            where += self.ge("mint",mint,True)
            where += self.le("mint",59,True)
            where += ") or ("
            or_condition = True
            year = t2.year
            month = t2.month
            day = t2.day
            hour = t2.hour

#       остаток периода
        where += self.eq("year",year,False)
        where += self.eq("month",month,True)
        where += self.eq("day",day,True)
        where += self.eq("hour",hour,True)
        where += self.le("mint",t2.minute,True)
        if(or_condition):
            where += self.ge("mint",0,True)
            where += ")"
        else:
            where += self.ge("mint",mint,True)

        rows = self.dbase.mins_select(where)
        return rows

#.......................................................
#   Метод формирования подстроки условия select данных часового графика
    def hget(self,year,month,day,hour,delta):

        t2 = ttime(year, month, day, hour, 0, 0)+timedelta(hours=delta)
        where = ""
        dday = day
        dmonth = month
        dyear = year
        h1 = hour
        h2 = t2.hour
        or_condition = False
        while(dday != t2.day):
            where += "("
            where += self.eq("year",year,False)
            where += self.eq("month",dmonth,True)
            where += self.eq("day",dday,True)
            where += self.ge("hour",h1,True)
            where += self.le("hour",23,True)
            where += ") or "            
            or_condition = True
            t0 = ttime(year, month, dday, 0, 0, 0)+timedelta(days=1)
            dday = t0.day
            dmonth = t0.month
            dyear = t0.year
            h1 = 0
            if(dday == t2.day):
                where += "("

        where += self.eq("year",dyear,False)
        where += self.eq("month",dmonth,True)
        where += self.eq("day",dday,True)
        where += self.le("hour",h2,True)
        if(or_condition):
            where += self.ge("hour",0,True)
            where += ")"
        else:
            where += self.ge("hour",hour,True)

        rows = self.dbase.hours_select(where)
        return rows

#.......................................................
#   Метод формирования подстроки условия select данных дневного графика
    def dget(self,year,month,day,delta):

        t2 = ttime(year, month, day, 0, 0, 0)+timedelta(days=delta)
        where = ""
        dday = day
        dmonth = month
        dyear = year
        or_condition = False
        while(dmonth != t2.month):
            where += "("
            where += self.eq("year",year,False)
            where += self.eq("month",dmonth,True)
            where += self.ge("day",dday,True)
            where += ") or "
            or_condition = True
            m = dmonth+1
            if(m == 13):
                m=1
                year += 1
            t0 = ttime(year, m, 1, 0, 0, 0)
            dday = 1
            dmonth = t0.month
            dyear = t0.year
            if(dmonth == t2.month):
                where += "("

        where += self.eq("year",dyear,False)
        where += self.eq("month",dmonth,True)
        where += self.ge("day",dday,True)
        if(or_condition):
            where += self.le("day",t2.day,True)
            where += ")"
        else:
            where += self.le("day",t2.day,True)

        rows = self.dbase.days_select(where)
        return rows

#.......................................................
#   Метод формирования массива координат времени
    def indarr(self,rows,var):
        
        res = []
        if(var == 1):
            for row in rows:
                res.append(str(row[5])+"-"+str(row[6])+"-"+str(row[7])+" "+str(row[8])+":"+str(row[9]))
        elif(var == 2):
            for row in rows:
                res.append(str(row[5])+"-"+str(row[6])+"-"+str(row[7])+" "+str(row[8])+":0")
        elif(var == 3):
            for row in rows:
                res.append(str(row[5])+"-"+str(row[6])+"-"+str(row[7])+" 0:0")

#        print(res)
        return res

#.......................................................
#   Метод формирования массива координат свечей
    def bodyarr(self,rows,var):
        
        res = {"open":[],'high':[],'low':[],'close':[],'volume':[]}
        if(var == 1):
            for row in rows:
                res['open'].append(row[3])
                res['high'].append(row[2])
                res['low'].append(row[1])
                res['close'].append(row[4])
                res['volume'].append(row[10])
        elif(var == 2):
            for row in rows:
                res['open'].append(row[3])
                res['high'].append(row[2])
                res['low'].append(row[1])
                res['close'].append(row[4])
                res['volume'].append(row[9])
        else:
            for row in rows:
                res['open'].append(row[3])
                res['high'].append(row[2])
                res['low'].append(row[1])
                res['close'].append(row[4])
                res['volume'].append(row[8])

        return res

#.......................................................
#   Метод рассчета параметров отрисовки
    def calc(self,rows):

        ind_arr = self.indarr(rows)
        body_arr = self.bodyarr(rows)
        d_array = pd.DatetimeIndex(data=ind_arr)
        df = pd.DataFrame(data=body_arr,index=d_array)

        return df


#.......................................................
#   Метод формирования подстроки равенства
#   s - строка наименования поля
#   p - значение условия
#   c - признак продолжения условия
    def eq(self,s,p,c):
        
        ret = ""
        if(c):
            ret += " AND "
        ret += s +"='"+str(p)+"'"
        
        return ret

#.......................................................
#   Метод формирования подстроки больше или равно
#   s - строка наименования поля
#   p - значение условия
#   c - признак продолжения условия
    def ge(self,s,p,c):
        
        ret = ""
        if(c):
            ret += " AND "
        ret += s +">='"+str(p)+"'"
        
        return ret

#.......................................................
#   Метод формирования подстроки меньше или равно
#   s - строка наименования поля
#   p - значение условия
#   c - признак продолжения условия
    def le(self,s,p,c):
        
        ret = ""
        if(c):
            ret += " AND "
        ret += s +"<='"+str(p)+"'"
        
        return ret