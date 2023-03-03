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
from trader import trader


# ******************** задание ********************
pair = "EURUSD"

# Пределы времени для теста
t1 = {'year':2021, 'month':8, 'day':10, 'hour':23}
t2 = {'year':2021, 'month':8, 'day':11, 'hour':23}

# Учитывать особенность конкретного метатрейдера!
time_shift = 0

# определение времени
time1 = ttime(t1['year'],t1['month'],t1['day'],t1['hour'],0,0)
time2 = ttime(t2['year'],t2['month'],t2['day'],t2['hour'],0,0)
time1 += timedelta(hours=time_shift)
time2 += timedelta(hours=time_shift)

mt5.initialize()

# объект-источник данных: здесь архивный
src = source(pair,time1,time2)
# создание торгующего объекта
trd = trader(pair,src)
trd.do()

# звук в конце работы        
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

raise SystemExit


# Выход из сделки - персмотреть, нужен ли этот vector?