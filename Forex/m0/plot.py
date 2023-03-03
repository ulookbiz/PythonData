import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------------
# Класс черчения свечного графика
#--------------------------------------------
class Plot():

# --------------------------------
#   Инициализатор
    def __init__(self):

        self.x = np.array([])
        self.close = np.array([])
        self.color = np.array([])
        self.open = np.array([])
        self.high = np.array([])
        self.low = np.array([])
        
        return

# --------------------------------
# Метод приема свечи 
    def candle(self,c):

        self.x = np.append(self.x,c['time'])
        self.high = np.append(self.high,c['high'])
        self.low = np.append(self.low,c['low'])
        self.close = np.append(self.close,c['close'])
        self.open = np.append(self.open,c['open'])
        if(c['close'] > c['open']):
            self.color = np.append(self.color,'w')
        else:
            self.color = np.append(self.color,'k')

        return

# --------------------------------
# Метод отрисовки графика
    def show(self):

        fig, ax = plt.subplots()
        ax.bar(self.x,self.close-self.open,bottom=self.open,color=self.color,
               edgecolor = 'black',linewidth = 1,width=5)

        for k,el in np.ndenumerate(self.x):
            x = np.array([self.x[k],self.x[k]])            
            if(self.close[k] > self.open[k]):
                y = np.array([self.high[k],self.close[k]])
                plt.plot(x,y,color='k')
                y = np.array([self.low[k],self.open[k]])
                plt.plot(x,y,color='k')
            else:
                y = np.array([self.high[k],self.open[k]])
                plt.plot(x,y,color='k')
                y = np.array([self.low[k],self.close[k]])
                plt.plot(x,y,color='k')

        plt.show()
        
        return

# --------------------------------
# Метод очистки массивов
    def clear(self):
        
        pass
        return

#plot = Plot()
#plot.candle({'time':0,'high':10,'low':3,'open':5,'close':9})
#plot.candle({'time':10,'high':12,'low':1,'open':9,'close':3})
#plot.candle({'time':20,'high':15,'low':3,'open':3,'close':7})
#plot.candle({'time':30,'high':7,'low':5,'open':7,'close':5})
#plot.candle({'time':40,'high':10,'low':3,'open':5,'close':9})
#plot.candle({'time':50,'high':12,'low':1,'open':9,'close':3})
#plot.candle({'time':60,'high':15,'low':3,'open':3,'close':7})
#plot.candle({'time':70,'high':7,'low':5,'open':7,'close':5})
#plot.candle({'time':80,'high':10,'low':3,'open':5,'close':9})
#plot.candle({'time':90,'high':12,'low':1,'open':9,'close':3})
#plot.candle({'time':100,'high':15,'low':3,'open':3,'close':7})
#plot.candle({'time':110,'high':7,'low':5,'open':7,'close':5})
#plot.candle({'time':120,'high':10,'low':3,'open':5,'close':9})
#plot.candle({'time':130,'high':12,'low':1,'open':9,'close':3})
#plot.candle({'time':140,'high':15,'low':3,'open':3,'close':7})
#plot.candle({'time':150,'high':7,'low':5,'open':7,'close':5})

#plot.show()


# ключевые операнды:
# x - np-массив
# y - np-массив
# fig, ax = plt.subplots()
# ax.bar(x,y) - построение баров
# fig.set_figwidth(12)    #  ширина Figure
# fig.set_figheight(6)    #  высота Figure
# fig.set_facecolor('floralwhite')
# задание нижнего края:
# ax.bar(x1, y1, width=0.2, bottom=1)
# задание нижних краев массивом массивом:
# ax.bar(x, y, bottom = bottom_rectangle)
# задание цвета бара:
# ax.bar(x, y, color = 'red')
# задание цвета баров массивом:
# color_rectangle = np.random.rand(7, 3)    # RGB
# ax.bar(x, y, color = color_rectangle)
# выделение границ баров
# ax.bar(x, y,
#       color = 'chartreuse',
#       edgecolor = 'darkblue',
#       linewidth = 5)
# начертание погрешностей:
# y_error = np.random.randint(5, 20, size = (2, 7))/15    
# ax.bar(x, y, 
#       yerr = y_error,      #  границы погрешностей
#       ecolor = 'darkred',  #  цвет линии погрешности
#       capsize = 10,        #  горизонтальная черточка
#       edgecolor = 'red',   #  цвет края прямоугольника
#       linewidth = 2,       #  ширина крайней линии
#       color = 'seashell',  #  цвет прямоугольника
#       linestyle = '--')    #  начертание линии

# plt.show()

#x1 = np.arange(1, 8)-0.2
#x2 = np.arange(1, 8)+0.2
#y1 = np.random.randint(1, 10, size = 7)
#y2 = np.random.randint(1, 10, size = 7)

#fig, ax = plt.subplots()

#ax.bar(x1, y1, width=0.2, bottom=1)
#ax.bar(x2, y2, width=0.2, bottom=2)

#ax.set_facecolor('seashell')
#fig.set_figwidth(12)    #  ширина Figure
#fig.set_figheight(6)    #  высота Figure
#fig.set_facecolor('floralwhite')

#plt.show()