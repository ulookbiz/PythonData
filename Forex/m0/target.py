#........................................................
#   Модуль, создающий задание
# уровни цен, контролируемые на факт достижения
# upwards or topdown
#........................................................
import json
import MetaTrader5 as mt5

#........................................................
# задание
#data = [
#         { "pair":"GBPUSD", "price":1.37, "direction":"topdown" },
#         { "pair":"EURUSD", "price":1.1466, "direction":"upwards" },
#         { "pair":"ETHUSD", "price":3110, "direction":"topdown" },
#         { "pair":"ETHUSD", "price":3100, "direction":"upwards" },
#         {"m1":1,"m5":0,"m15":0,"m30":0,"h1":0,"d1":0},
#       ]
#with open("target.json", "w") as write_file:
#    json.dump(data, write_file)


fp = open("target.json", "r")
data = json.load(fp)

prs = []
prices = []
for dt in data:
    if "pair" in dt:
        if dt['pair'] not in prs:
            prs.append(dt['pair'])
        prices.append(dt)
    else:
        timeframes = dt

print(prs)
print(prices)
print(timeframes)

raise SystemExit