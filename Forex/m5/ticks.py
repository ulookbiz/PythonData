import MetaTrader5 as mt5
from datetime import datetime, date, time
from chart import chart

#........................................................
# Класс, подающий тики прошедшего периода
class ticks():
# --------------------------------
#   Инициализатор
    def __init__(self,pair):

        self.pair = pair
#       объекты свечей
#       объекты коллекций свечей    

        mt5.initialize()

        return




#   Обработчик тиков
    def put(self,tick):

#       первый тик
        if(self.firsttick == True):
            self.firsttick = False
            self.bid = tick['bid']
            self.ask = tick['ask']
            self.sec = tick['sec']
            self.day = tick['day']
            self.hour = tick['hour']
            self.mint = tick['min']
            self.cyear = tick['year']
            self.cmonth = tick['month']


#       учет тика в минутной свече
        if(self.mint != tick['min']):
#           завершение формирования минутной свечи
            self.mCandle.cclose()
            self.cndl = self.mCandle.get()
            self.cndl['year'] = self.cyear
            self.cndl['month'] = self.cmonth
            self.cndl['day'] = self.day
            self.cndl['hour'] = self.hour
            self.cndl['min'] = self.mint
            self.mCandles.put(self.cndl)
            if(self.mdb):
                self.dbsend('m',self.cndl)

            self.mCandle = M1candle()
            self.mint = tick['min']

        self.mCandle.put(tick)

#       учет тика в часовой свече
        if(self.hour != tick['hour']):
#           завершение формирования часовой свечи
            self.hCandle.cclose()
            self.cndl = self.hCandle.get()
            self.cndl['year'] = self.cyear
            self.cndl['month'] = self.cmonth
            self.cndl['day'] = self.day
            self.cndl['hour'] = self.hour
            self.hCandles.put(self.cndl)
            if(self.hdb):
                self.dbsend('h',self.cndl)

            self.hCandle = H1candle()
            self.hour = tick['hour']

        self.hCandle.put(tick)

#       учет тика в дневной свече
        if(self.day != tick['day']):
#           завершение формирования дневной свечи
            self.dCandle.cclose()
            self.cndl = self.dCandle.get()
            self.cndl['year'] = self.cyear
            self.cndl['month'] = self.cmonth
            self.cndl['day'] = self.day
            self.dCandles.put(self.cndl)
            if(self.ddb):
                self.dbsend('d',self.cndl)

            self.dCandle = D1candle()
            self.day = tick['day']

        self.dCandle.put(tick)

        return

#   Завершение обработки
    def complete(self):

        self.cndl = self.mCandle.get()
        self.cndl['year'] = self.cyear
        self.cndl['month'] = self.cmonth
        self.cndl['day'] = self.day
        self.cndl['hour'] = self.hour
        self.cndl['min'] = self.mint
        self.mCandles.put(self.cndl)
        if(self.mdb):
            self.dbsend('m',self.cndl)

        self.cndl = self.hCandle.get()
        self.cndl['year'] = self.cyear
        self.cndl['month'] = self.cmonth
        self.cndl['day'] = self.day
        self.cndl['hour'] = self.hour
        self.hCandles.put(self.cndl)
        if(self.hdb):
            self.dbsend('h',self.cndl)

        self.cndl = self.dCandle.get()
        self.cndl['year'] = self.cyear
        self.cndl['month'] = self.cmonth
        self.cndl['day'] = self.day
        self.dCandles.put(self.cndl)
        if(self.ddb):
            self.dbsend('d',self.cndl)

        self.db.commit()

        return

#   Запись свечи в базу данных
    def dbsend(self,frame,cndl):

        if(frame == 'm'):
            self.db.msave(cndl)
        elif(frame == 'h'):
            self.db.hsave(cndl)
        else:
            self.db.dsave(cndl)

        return

#   Очистка таблиц в заданном периоде
    def tbclear(self,year,month,day):

        condition = "year='"+str(year)+"' and month='"+str(month)+"' and day='"+str(day)+"'"
        self.db.clear("mins",condition)
        self.db.clear("hours",condition)
        self.db.clear("days",condition)
        
        return

#........................................................
# Класс, подающий тики прошедшего периода
class oldTicks(ticks):

#   Метод обработки данных за 1 день
    def day(self,year,month,day):

        bid = ask = sec = None
        cnt = 0        
        tim = period(year,month,day)
        ticks = mt5.copy_ticks_range(self.pair, tim['start'], tim['end'], mt5.COPY_TICKS_ALL)

        if(len(ticks) == 0):
            return

#        for t in ticks:
#            tick = noll_2(t)
#            if(tick['day'] != 2):
#                continue
#            if(tick['hour'] < 21 or (tick['hour']  == 21 and tick['min'] < 59)):
#                continue
#            if(tick['min'] == 59 and tick['sec'] < 59):
#                continue
#            if(tick['hour'] > 22 or (tick['hour']  == 22 and tick['min'] > 0)):
#               continue
#            if(tick['hour'] == 22 and tick['sec'] > 11):
#                continue
#            print(tick)
#        return    


        do_complete = False
        for t in ticks:
            tick = noll_2(t)
            if(tick['day'] != day):
                continue
            cnt += 1            
#           отработка счетчиков
            if(tick['bid'] != bid or tick['ask'] != ask or tick['sec'] != sec):
                tick["volume"] = cnt
                self.put(tick)
                bid = tick['bid']
                ask = tick['ask']
                sec = tick['sec']
                cnt = 0
                do_complete = True
        if(do_complete):
            self.complete()
            
        return


