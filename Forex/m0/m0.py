#........................................................
#   Главный модуль
#........................................................
import numpy as np
import json
from time import sleep
import MetaTrader5 as mt5
from charter import Charter
from prevData import M1data,M5data,M15data,M30data,H1data,H4data,D1data
from abcer import ABCer
from trtg import toReachTheGoal
from speed import checkspeed
from timer import Timer
from source import ticksSource
from sound import Sound
from funcs import escape


#**********************************************************
# Главная функция
#**********************************************************
def main(to_ABC, to_trtg, to_speed):

#........................................................
# задание, чтение из файла
    fp = open("target.json", "r")
    data = json.load(fp)
    all_pairs = []

#........................................................
#........................................................
# Циклы создания "плоских массивов"
#........................................................
# условная подготовка контроля достижения целей цен
    if(to_trtg):
        targets = []
        tprices = []
        for dt in data[0]['target']:
            if(dt['active'] == 1):
                pair = dt['pair']
                targets.append(pair)
                tprices.append({'pair':dt['pair'],'price':dt['price'],
                                'direction':dt['direction']})
                all_pairs.append(pair)
        trg = toReachTheGoal()
        trg.activate(tprices)

        print("Задание: ожидать достижение цены:")
        for p in tprices:
            print(p['pair'],": ",p['price'],p['direction'])
        print("---")




#........................................................
# условная подготовка контроля скоростей
    if(to_speed):
        speeds = []
        intervals = []
        for dt in data[1]['speed']:
            if(dt['active'] == 1):
                pair = dt['pair']
                speeds.append(pair)
                interval = ['m1','m5','m15','m30','h1','h4','d1']
                if(dt['interval'] == 5):
                    interval.pop(0)
                if(dt['interval'] == 15):
                    interval.pop(0)
                    interval.pop(0)
                if(dt['interval'] == 30):
                    interval.pop(0)
                    interval.pop(0)
                    interval.pop(0)
                intervals.append(interval)
                if pair not in all_pairs:
                    all_pairs.append(pair)

        sp = checkspeed()
        sp.activate(speeds)

        print("Задание контроля скорости изменения цен:")
        for s in speeds:
            print(s)
        print("---")

#........................................................
# условная подготовка построения графиков
    if(to_Chart):
        chart_width = 60
        timeframes = {} # не определено
#      запуск системы графиков
        tfs = []
        for key in timeframes.keys():
            if(timeframes[key] == 1):
                tfs.append(key)
#      подготовка рабочих графиков
        charter = Charter(prs,tfs,chart_width)

#      объекты старых данных
        M1data = M1data(chart_width)
        M5data = M5data(chart_width)
        M15data = M15data(chart_width)
        M30data = M30data(chart_width)
        H1data = H1data(chart_width)
        H4data = H4data(chart_width)
        D1data = D1data(chart_width)
        for p in prs:
            for t in tfs:
                if(t == 'd1'):
                    data = D1data.get(p)
                elif(t == 'h4'):
                    data = H4data.get(p)
                elif(t == 'h1'):
                    data = H1data.get(p)
                elif(t == 'm30'):
                    data = M30data.get(p)
                elif(t == 'm15'):
                    data = M15data.get(p)
                elif(t == 'm5'):
                    data = M5data.get(p)
                elif(t == 'm1'):
                    data = M1data.get(p)
                    charter.add(p,t,data)

#   отработанные объекты
        del M1data
        del M5data
        del M15data
        del M30data
        del H1data
        del H4data
        del D1data

#........................................................
# условный запуск поиска ABC
    if(to_ABC):
        abc = ABCer(prs)


#........................................................
#........................................................
#   Цикл таймера

# текущее отслеживание с отрезками времени
    src = ticksSource()
    work_time = 3600 # количество секунд работы
    time_out = 0.2 # перерыв между обработкой очередной пары
    timer = Timer(work_time)
    sound = Sound()

    while(timer.close == False):

#........................................................
#      Цикл перебора валютных пар
        for p in all_pairs:
#          выход по esc
            escape()

#          цикл по парам
            tick = src.get(p)
            if(tick != None):
#              рассылка тиков в инструменты
                if(to_Chart):
#                  тик для графиков
                    charter.put(p,tick)
                
                if(to_ABC):
#                  тик для анализатора ABC
                    abc.put(p,tick)

                if(to_trtg):
#                  тик для анализатора toReachTheGoal
                    answer = trg.put(p,tick)
                    if(answer != False):
                        print(answer)
                        sound.event()

                if(to_speed):
#                  тик для анализатора checkspeed
                    if p in speeds:
                        sp.put(p,tick)

#          пауза
            sleep(time_out)
        
#   обработка времени и формирование обобщения
        tm = timer.check()
        if(tm != False):
            print("m0: tm=",tm)
            for p in all_pairs:
#              выход по esc
                escape()

#              обобщения
                if(to_Chart):
#                  для графиков
                    charter.generalization(p,tm)
                
                if(to_ABC):
#                  для анализатора ABC
                    abc.generalization(p)

                if(to_speed):
#                  для анализатора скорости
                    if p in speeds:
                        ind = speeds.index(p)
                        if(tm in intervals[ind]):
                            sp.generalization(p,tm)
                
    sound.finish()


#**********************************************************
# начало работы
#**********************************************************
# ограничения
# построение графиков
to_Chart = False
# запуск анализатора ABC
to_ABC = False
# запуск проверки достижения цели в цене
to_trtg = False
# запуск проверки скорости изменения цен
to_speed = True
# инициализация метатрейдера
mt5.initialize()

main(to_ABC, to_trtg, to_speed)

raise SystemExit
