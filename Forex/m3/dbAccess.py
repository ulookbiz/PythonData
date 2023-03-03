from funcs import ttime
import pandas as pd
from datetime import timedelta
from dbase import dbase

#........................................................
# Класс, формирующий данные для построения графика
class dbData():
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
    def hget(self,year,month,day,hour):

        where = "year='"+str(year)+"' and month='"+str(month)+"' "
        where += "and day='"+str(day)+"' and hour='"+str(hour)+"'"
        rows = self.dbase.hours_select(where)
        if(len(rows) > 0):
            return rows[0]
        else:
            return False

#.......................................................
#   Метод формирования подстроки условия select данных дневного графика
    def dget(self,year,month,day):

        where = "year='"+str(year)+"' and month='"+str(month)+"' and day='"+str(day)+"'"
        rows = self.dbase.days_select(where)
        if(len(rows) > 0):
            return rows[0]
        else:
            return False

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