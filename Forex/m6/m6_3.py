#........................................................
# Включение рынка:
#   - определено задание
#   - формируется структура объектов графика
#   - подтягиваются старые данные из сети
#   - запускается мониторинг новых тиков
#........................................................
import MetaTrader5 as mt5
import winsound
from time import sleep
from chart import chart
from netdata import netDataProcessing
from newTicks import newTicks

#import datetime
#from datetime import datetime
#import pytz
#t1 = datetime.now()
#y = t1.year
#m = t1.month
#d = t1.day
#h = t1.hour
#print(t1)
#timezone = pytz.timezone("Etc/UTC")
#t1 = datetime(y, m, d, h, tzinfo=timezone)
#print(t1)
#raise SystemExit

# ******************** задание ********************
#pairs = {"EURUSD","GBPJPY"}
pairs = {"EURUSD"}
#pairs = {"DASHUSD","EOSUSD","ETHUSD"}
chart_width = 60
timeframes = {"d1","h1","m1"}
# ------------------- задание --------------------

# ассоциативный массив, в котором каждый элемент является массивом,
# содержащим объекты-графики и объект наполнения этих графиков
charts = dict()

# Создание объектов графиков и обработки тиков
for pair in pairs:
    
    charts[pair] = dict()
#   объект для получения старых свечей для каждой пары из сети
    nd = netDataProcessing(pair)
#   объект для обработки новых тиков для каждой пары
    nt = newTicks(pair)
    if(nt == False):
        print("Нет входящих тиков. Стоп")
        raise SystemExit
    
    for tf in timeframes:
 #      график для каждого таймфрейма
        chrt = chart(tf,chart_width)
#       добавление графика в объект обработки данных из сети
        nd.chart_add(chrt)
#       добавление графика в объект обработки новых тиков
        nt.chart_add(chrt)
#       добавление графика в двумерный массив графиков
        charts[pair][tf] = chrt
#   добавление объекта обработки старых данных из сети
    charts[pair]['nd'] = nd
#   добавление объекта обработки новых тиков из сети
    charts[pair]['nt'] = nt
    
# далее может быть использован класс MT5
mt5.initialize()

# наполнение графиков прошлыми данными
for pair in pairs:
    charts[pair]['nd'].do()
    pass

#raise SystemExit

# Обработка текущих тиков
for i in range(3000):
    for key in charts:
        charts[key]['nt'].do3("Scalp!")
    sleep(0.2)

#raise SystemExit

for ch in charts:
#    print(ch)
    for c in charts[ch]:
#        if(c == "d1" or c == "h1" or c == "m1"):
        if(c == "d1"):
#            charts[ch][c].dump()
#            charts[ch][c].chart_plot()
#            charts[ch][c].chart_speed()
            pass
        
        
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
        
raise SystemExit
# 1. 
# 2. Решить вопрос учета таймфреймов, отличных от d1,h1,m1
# 3. Посмотреть, как в обработке тиков формировать спред свечей
