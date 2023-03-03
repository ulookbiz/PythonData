#........................................................
# Оюработка архивных тиков для записи их в БД
# Для часовых и дневных данных используется метод copy_rates_from
# из MT5, считываются готовые свечи (метод result)
# Для минутных данных используется метод copy_ticks_range из MT5,
# считываются тики (метод result2)
#........................................................
from oldData import oldDataProcessing
from dbase import dbase
import MetaTrader5 as mt5

#........................................................
# Задание для выполнения обработки данных за месяц
pairs = []
timeframes = []

year = 2021
month = 6
pairs.append("EURUSD")
#pairs.append("GBPJPY")
timeframes.append("d1")
timeframes.append("h1")
timeframes.append("m1")

mt5.initialize()

#.......................................................
for pair in pairs:
    db = dbase(pair,year,month)
    db.monthclear(year,month)
    for timeframe in timeframes:
        od = oldDataProcessing(pair,timeframe,year,month)
        if(timeframe == 'd1'):
            pass
            result = od.result()
            db.put_d1(result)
        elif(timeframe == 'h1'):
            pass
            result = od.result()
            db.put_h1(result)
        else:
            while(True):
#               цикл обработки почасово                
                result = od.result2()
                if(result == "End"):
                    break
                if(result == None):
#                   оставляет возможность проверить следующие дни
                    continue
                db.put_m1(result)
#........................................................

mt5.shutdown()
raise SystemExit