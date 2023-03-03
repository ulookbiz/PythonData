from datetime import datetime
import MetaTrader5 as mt5
# выведем данные о пакете MetaTrader5
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# импортируем модуль pandas для вывода полученных данных в табличной форме
import pandas as pd
pd.set_option('display.max_columns', 500) # сколько столбцов показываем
pd.set_option('display.width', 1500)      # макс. ширина таблицы для показа
# импортируем модуль pytz для работы с таймзоной
import pytz
 
# установим подключение к терминалу MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# установим таймзону в UTC
timezone = pytz.timezone("Etc/UTC")
# создадим объект datetime в таймзоне UTC, чтобы не применялось смещение локальной таймзоны
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# получим 10 баров с EURUSD H4 начиная с 01.10.2020 в таймзоне UTC
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)

# завершим подключение к терминалу MetaTrader 5
mt5.shutdown()
# выведем каждый элемент полученных данных на новой строке
#print("Выведем полученные данные как есть")
#for rate in rates:
#    print(rate)

# создадим из полученных данных DataFrame
rates_frame = pd.DataFrame(rates)

#raise SystemExit
# сконвертируем время в виде секунд в формат datetime
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

print(rates_frame)                  
         
# выведем данные
print("\nВыведем датафрейм с данными")
print(rates_frame)