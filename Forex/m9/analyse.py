from pair_ch import pair_ch

# Класс "Анализ"
class analyse():

# --------------------------------
#   Инициализатор
    def __init__(self):

        self.pr = None
        
        return
    
# --------------------------------
#   Метод общий анализа
    def do(self,pair,chart):

        self.pair = pair    # рабочая пара
        self.chart = chart  # объект графика
        self.pr = pair_ch(self.pair) # объект данных пары

        self.fwaves() # найти фигуру 1-2-3
#        self.ext() # найти экстремумы
#        self.capture()

#        print()
    
        return

# --------------------------------
#   Метод поиска экстремумов
    def ext(self):
        
        length = len(self.chart.candles)
        timef = self.chart.timef
        max_high = 0
        min_low = 9999
        
        for i in range(0,length):
            cndl = self.chart.candles[i]
            if(max_high < cndl.high):
                max_high = cndl.high
                ihigh = i
            if(min_low > cndl.low):
                min_low = cndl.low
                ilow = i

        print(self.pair,":",timef,":","максимум графика:",max_high,"i=",ihigh)
        print(self.pair,":",timef,":","минимум графика:",min_low,"i=",ilow)
        
        return

# --------------------------------
#   Метод определения волн по фракталам
    def fwaves(self):
        
        length = len(self.chart.candles)
        if(length == 0):
            return

#       определение последних волн по фракталам
        p1 = p2 = p3 = None
        p0 = {"ind":0,"side":None,"high":self.chart.candles[0].high,
              "low":self.chart.candles[0].low}
        for i in range(length):
#           цикл формирования фигуры p1-p2-p3            
            c = self.chart.candles[i]
            if(c.upFr):
                
                print("up:",i)

                if(p3 == None):
                    p3 = {"ind":i,"side":1,"value":self.chart.candles[i].high}
                elif(p3['side'] == 1 and p2 == None):
#                   возможно, переопределяется p3
                    if(self.chart.candles[i].high > p3['value']):
                        p3 = {"ind":i,"side":1,"value":self.chart.candles[i].high}
                elif(p3['side'] == -1 and p2 == None):
                    p2 = {"ind":i,"side":1,"value":self.chart.candles[i].high}

                elif(p2['side'] == 1 and p1 == None):
#                   возможно, переопределяется p2
                    if(self.chart.candles[i].high > p2['value']):
                        p2 = {"ind":i,"side":1,"value":self.chart.candles[i].high}
                elif(p2['side'] == -1 and p1 == None):
                    p1 = {"ind":i,"side":1,"value":self.chart.candles[i].high}
#                   завершение фигуры
                    break
                elif(p1['side'] == 1):
#                   возможно, переопределяется p1
                    if(self.chart.candles[i].high > p1['value']):
                        p1 = {"ind":i,"side":1,"value":self.chart.candles[i].high}
                    else:
#                       завершение фигуры
                        break

            if(c.downFr):

                print("down:",i)                

                if(p3 == None):
                    p3 = {"ind":i,"side":-1,"value":self.chart.candles[i].low}
                elif(p3['side'] == -1 and p2 == None):
#                   возможно, переопределяется p3
                    if(self.chart.candles[i].low < p3['value']):
                        p3 = {"ind":i,"side":-1,"value":self.chart.candles[i].low}
                elif(p3['side'] == 1 and p2 == None):
                    p2 = {"ind":i,"side":-1,"value":self.chart.candles[i].low}

                elif(p2['side'] == -1 and p1 == None):
#                   возможно, переопределяется p2
                    if(self.chart.candles[i].low < p2['value']):
                        p2 = {"ind":i,"side":-1,"value":self.chart.candles[i].low}
                elif(p2['side'] == 1 and p1 == None):
                    p1 = {"ind":i,"side":-1,"value":self.chart.candles[i].low}
#                   завершение фигуры
                    break
                elif(p1['side'] == -1):
#                   возможно, переопределяется p1
                    if(self.chart.candles[i].low < p1['value']):
                        p1 = {"ind":i,"side":-1,"value":self.chart.candles[i].low}
                    else:
#                       завершение фигуры
                        break
            
        p0['high'] = round(p0['high']*self.pr.mult,1)
        p0['low'] = round(p0['low']*self.pr.mult,1)
        p1['value'] = round(p1['value']*self.pr.mult,1)
        p2['value'] = round(p2['value']*self.pr.mult,1)
        p3['value'] = round(p3['value']*self.pr.mult,1)
        print("Точки 1-2-3:")
        
        if(p1['side'] == 1):
            d1 = p1['value']-p2['value']
            d2 = p3['value']-p2['value']
            if(d1 > d2):
                print("Фигура 1-2-3 вниз")
            elif(d1 < d2):
                print("Фигура 1-2-3 пробой вверх")
            else:
                print("Фигура 1-2-3 равновесная")
        else:
            d1 = p2['value']-p1['value']
            d2 = p2['value']-p3['value']
            if(d1 > d2):
                print("Фигура 1-2-3 вверх")
            elif(d1 < d2):
                print("Фигура 1-2-3 пробой вниз")
            else:
                print("Фигура 1-2-3 равновесная")

        d1 = round(p2['value']-p1['value'],1)
        d2 = round(p3['value']-p2['value'],1)
        print("1:","-",p1['ind'],"-",p1['value'])
        print("2:","-",p2['ind'],"-",p2['value'],"d=",d1)
        print("3:","-",p3['ind'],"-",p3['value'],"d=",d2)
        
        print("Последние изменения")
        if(p3['side'] == 1):
            if(p0['high'] > p3['value']):
                print("Последняя волна вверх продолжается")
            else:
                print("Последняя волна вверх развернулась")
            d1 = round(p0['high']-p3['value'],1)
            print(":",p0['high'],"d=",d1)
        else:
            if(p0['low'] < p3['value']):
                print("Последняя волна вниз продолжается")
            else:
                print("Последняя волна вниз развернулась")
            d1 = round(p0['low']-p3['value'],1)
            print(":",p0['low'],"d=",d1)
        
        return

# --------------------------------
#   Метод проверки значительного поглощения предыдущей свечи
    def capture(self):

        cndl0 = self.chart.candles[0]
        cndl1 = self.chart.candles[1]
#       знак минус - для свечи вниз
        d0 = round((cndl0.close - cndl0.open)*self.pr.mult)
        d1 = round((cndl1.close - cndl1.open)*self.pr.mult)
        if(d0*d1 < 0):
#           разное направление
            if(abs(d0)-abs(d1) > self.pr.significant_value):
                print("Поглощение!",self.pair,self.chart.timef)

        return