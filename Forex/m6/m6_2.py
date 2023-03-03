#........................................................
# Мониторинг рынка (много пар одновременно)
#........................................................
import MetaTrader5 as mt5
from time import sleep
from chart import chart
from newTicks import newTicks

#pairs = {"EURUSD","USDJPY","EURJPY"}
pairs = {"DASHUSD","EOSUSD","ETHUSD"}

# ассоциативный массив, в котором каждый элемент является массивом,
# содержащим объекты-графики и объект наполнения этих графиков
charts = dict()

mt5.initialize()

# Создание объектов графиков и обработки тиков
for pair in pairs:
    dChart = chart("d1")
    hChart = chart("h1")
    mChart = chart("m1")    
    nt = newTicks(pair)
    if(nt == None):
        print("Нет входящих тиков. Стоп")
        raise SystemExit
    nt.chart_add(dChart)
    nt.chart_add(hChart)
    nt.chart_add(mChart)
    charts[pair] = {"d1":dChart,"h1":hChart,"m1":mChart,"nt":nt}

#print(charts)
#raise SystemExit

# Обработка текущих тиков
for i in range(80):
    for key in charts:
        charts[key]['nt'].do3()
    sleep(0.2)
    

raise SystemExit