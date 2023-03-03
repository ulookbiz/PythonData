#........................................................
# Мониторинг рынка (одна пара)
#........................................................
import MetaTrader5 as mt5
from datetime import timedelta
import datetime
from chart import chart
from newTicks import newTicks
from oldTicks import oldTicks
from funcs import ttime

pair = "ETHUSD"

mt5.initialize()

# Текущий момент времени
now = datetime.datetime.now()
#print(now)

# Расчет момента времени для подготовки предыдущих свеч:
# за предыдущие 10 дней, 10 часов, 10 минут
y = (now+timedelta(days=-30)).year
m = (now+timedelta(days=-30)).month
td = now+timedelta(days=-30) # крайний срок отсчета последних прошедших дней
th = now+timedelta(hours=-30) # крайний срок отсчета последних прошедших часов
tmi = now+timedelta(minutes=-30) # крайний срок отсчета последних прошедших минут
start = ttime(y,m,td.day,0,0,0)

# Создание объектов графиков
mChart = chart("m1")
dChart = chart("d1")
hChart = chart("h1")

# Обработка старых данных
ot = oldTicks("ETHUSD")
ot.chart_add(dChart)
ot.chart_add(hChart)
ot.chart_add(mChart)
ot.limit(td,th,tmi) # ограничения 

# Прием и обработка новых тиков
nt = newTicks("ETHUSD")
nt.chart_add(dChart)
nt.chart_add(hChart)
nt.chart_add(mChart)

# Обновленный текущий момент времени
now = datetime.datetime.now()

# Обработка старых тиков
ot.do(start,now)
raise SystemExit
# доработка пропущенного времени
ot.limit(now,now,now)
ot.do(now,datetime.datetime.now())
#raise SystemExit
# Обработка текущих тиков
nt.do()

# Текущая задача: сотладка m51
