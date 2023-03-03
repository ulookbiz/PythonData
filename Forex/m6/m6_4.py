#........................................................
# Проверка, тестовая, алгоритмов на прошедших торгах
#   Главный модуль
#   - определяет начальные условия
#   - запускает источник сигналов
#........................................................
from datetime import timedelta
import MetaTrader5 as mt5
import winsound
from funcs import ttime
from source import source
from area import area
from trader import trader
from advisor import advisor

# ******************** задание ********************
pair = "EURUSD"

# Пределы времени для теста
t1 = {'year':2021, 'month':7, 'day':9, 'hour':1}
t2 = {'year':2021, 'month':7, 'day':9, 'hour':21}

# Учитывать особенность конкретного метатрейдера!
time_shift = 3

# определение времени
time1 = ttime(t1['year'],t1['month'],t1['day'],t1['hour'],0,0)
time2 = ttime(t2['year'],t2['month'],t2['day'],t2['hour'],0,0)
time1 += timedelta(hours=time_shift)
time2 += timedelta(hours=time_shift)

mt5.initialize()

# создание объекта-источника данных
source = source(pair,time1,time2)
# создание объекта-базы данных
area = area(pair)
# создание торгующего объекта
trader = trader(pair)
# создание объекта-советника по принятию решений
advisor = advisor()

# звук в конце работы        
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

raise SystemExit
