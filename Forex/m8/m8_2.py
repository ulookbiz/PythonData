# Компиляция файла G:\PythonData\Forex\m8\m8_2.py
#   G:
#   cd pyinstaller
#   pyinstaller G:\PythonData\Forex\m8\m8_2.py -F
#   numpy.core.multiarray failed to import
#
import numpy
import matplotlib
import MetaTrader5 as mt5
from win import winApp

#........................................................
# Мониторинг рынка (много пар одновременно)
#........................................................
task = winApp()
task.mainloop()

pairs = task.getpairs()
levels = task.getlevels()

print(pairs)
print(levels)
raise SystemExit

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

raise SystemExit
