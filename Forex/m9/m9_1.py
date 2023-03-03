#........................................................
#   Главный модуль, содержащий:
#       задание - список пар для анализа
#       объекты, формирующие структуру графика в памяти
#       объекты анализа графика и принятия торговых решений
#       метод отображения результатов работы
#   Сделано на базе m6_3
#........................................................
import MetaTrader5 as mt5
import winsound
import datetime
from time import sleep
from netdata import netDataProcessing
from newTicks import newTicks
from chart import chart
from analyse import analyse

# ******************** задание ********************
#pairs = {"EURUSD","GBPJPY","AUDNZD"}
#pairs = {"DASHUSD","EOSUSD","ETHUSD"}
pairs = {"EURUSD"}
chart_width = 60
#timeframes = {"d1","h4","h1","m30","m15","m5","m1"}
timeframes = {"h4"}

# ------------------- задание структур программы --------------------
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

# ------------------- работа с метатрейдером --------------------
# ------------------- наполнение графиков старыми данными --------------------
mt5.initialize()

# наполнение графиков прошлыми данными
for pair in pairs:
    charts[pair]['nd'].do()
    pass

# первый запуск анализа
an = analyse()
for pair in pairs:
    for tf in timeframes:
#        an.do(charts[pair][tf])
        an.do(pair,charts[pair][tf])
t = datetime.datetime.now()
d = t.day
h = t.hour
m = t.minute
    
#raise SystemExit
# ------------------- и выполнение объектов анализа торговли --------------------
for i in range(30):
#   отслеживание смены минуты, часа, дня
#   формирование контрольного массива cmas
    t = datetime.datetime.now()
    cmas = [] # массив таймфреймов, требуемых для обновления
    if(t.minute != m):
        cmas.append('m1')
        m = t.minute
        if(t.minute%5 == 0):
            cmas.append('m5')
            if(t.minute%15 == 0):
                cmas.append('m15')
                if(t.minute%30 == 0):
                    cmas.append('m30')
    if(t.hour != h):
        cmas.append('h1')
        h = t.hour
        if(t.hour%4 == 0):
            cmas.append('h4')
    if(t.day != d):
        cmas.append('d1')
        d = t.day

#   учет порции данных в графиках
    for key in charts:
        charts[key]['nt'].do3()

    if(len(cmas) == 0):
#       анализа не требуется
        sleep(0.2)
        continue
   
#   анализ требуется
    for key in charts:
        pr = charts[key]
        for key2 in pr:
            if key2 in cmas:
                an.do(key,charts[key][key2])

    sleep(0.2)
    
#raise SystemExit

for ch in charts:
#    print(ch)
    for c in charts[ch]:
#        print(c)
        if(c == "d1" or c == "h4" or c == "h1" or c == "m30"
        or c == "m15" or c == "m5" or c == "m1"):
#        if(c == "d1"):
#            charts[ch][c].dump()
            charts[ch][c].chart_plot()
#            charts[ch][c].dump()
#            charts[ch][c].chart_speed()
            pat = charts[ch][c].chart_iso()
    
#print(pat.patt)

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
        
raise SystemExit
