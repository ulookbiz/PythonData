"""Главный метод и класс, формирующий задание"""

from time import sleep
from chart import chart
from newTicks import newTicks
from check import check
import MetaTrader5 as mt5
import winsound

# Класс Задание
class Task():
# --------------------------------
#   Инициализатор
    def __init__(self):

        #self.pairs = {"EURUSD","USDJPY","EURJPY"}
        #pairs = {"DASHUSD","EOSUSD","ETHUSD"}
        self.pairs = {"EURUSD"}
        self.levels = [{"EURUSD":1.1824,"move":"-","line":"ask"}]

# --------------------------------
    def wpairs(self):
        return self.pairs

# --------------------------------
    def lcontrol(self):
        return self.levels


#=========================================
#........................................................
# Мониторинг рынка (много пар одновременно)
#  для
#........................................................
task = Task()
pairs = task.wpairs()
levels = task.lcontrol()

# ассоциативный массив, в котором каждый элемент является массивом,
# содержащим объекты-графики и объект наполнения этих графиков
charts = dict()
# ассоциативный массив, в котором каждый элемент является объектом
# одной пары
checks = dict()

if not mt5.initialize(): 
    print("initialize() failed, error code =",mt5.last_error()) 
    raise SystemExit

#print(mt5.terminal_info())   
#print(mt5.version())

raise SystemExit


# Создание объектов графиков, обработки тиков, контроля
for pair in pairs:
    dChart = chart("d1",60)
    hChart = chart("h1",60)
    mChart = chart("m1",60)
    nt = newTicks(pair)
    if nt is None:
        print("Нет входящих тиков. Стоп")
        raise SystemExit
    nt.chart_add(dChart)
    nt.chart_add(hChart)
    nt.chart_add(mChart)
    charts[pair] = {"d1":dChart,"h1":hChart,"m1":mChart,"nt":nt}

# Запуск системы контроля
for pair in pairs:
    checks[pair] = check(pair)
    for level in levels:
        params = []
        for item in level.items():
#            print(item)
            params.append(item[1])
        checks[pair].price_level_add(params[0],params[1],params[2])
#   внедрение объекта контроля в объект обработки тиков
    nt.check_add(checks[pair])

# Обработка текущих тиков
for i in range(80):
    for key in charts:
        charts[key]['nt'].do3()
    sleep(0.2)
#print(charts)

# звук в конце работы
FREQUENCY = 2500  # Set Frequency To 2500 Hertz
DURATION = 100  # Set Duration To 1000 ms == 1 second
winsound.Beep(FREQUENCY, DURATION)

raise SystemExit
