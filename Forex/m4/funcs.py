from datetime import datetime, date, time
from datetime import timedelta
#.......................................
# Функция преобразования пришедшего тика к стандартному виду
def noll_1(tick):
    
    time = datetime.fromtimestamp(tick.time).timetuple()
    mytick = {
              'year': time[0],
              'month': time[1],
              'day': time[2],
              'hour': time[3],
              'min': time[4],
              'sec': time[5],
              'bid': tick.bid,
              'ask': tick.ask  
             }
    return(mytick)

#.......................................
# Метод преобразования архивного тика к стандартному виду
def noll_2(tick):
    time = datetime.fromtimestamp(tick[0]).timetuple()
    mytick = {'year': time[0],
              'month': time[1],
              'day': time[2],
              'hour': time[3],
              'min': time[4],
              'sec': time[5],
              'bid': round(tick[1],5),
              'ask': round(tick[2],5)
             }
    return(mytick)

#.......................................
# Функция преобразования данных времени во внутренний формат
def ttime(year, month, day, hour, minu, sec):

    d = date(year,month,day)
    t = time(hour,minu,sec)
    dt = datetime.combine(d, t)

    return dt

#.......................................
# Функция формирования периода времени в 1 день
def period(year, month, day):

    t1 = ttime(year,month,day,0,0,0)
    t2 = ttime(year,month,day,0,0,0)+timedelta(days=1)
    
    return {"start":t1,"end":t2}