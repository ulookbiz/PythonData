from datetime import datetime, timedelta
import pytz

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
              'bid': round(tick.bid,5),
              'ask': round(tick.ask,5)
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

#    timezone = pytz.timezone("Etc/UTC")
#    dt = datetime(year,month,day,hour,minu,sec,tzinfo=timezone)
    dt = datetime(year,month,day,hour,minu,sec)

    return dt

#.......................................
# Функция формирования периода времени в 1 день
def period(year, month, day):

    t1 = ttime(year,month,day,0,0,0)
    t2 = ttime(year,month,day,0,0,0)+timedelta(days=1)
    
    return {"start":t1,"end":t2}

#.......................................
# Функция расчета количество секунд в отрезке времени
def duration(time1,time2):

    duration = time2-time1
    result = round(duration.total_seconds())
    
    return result