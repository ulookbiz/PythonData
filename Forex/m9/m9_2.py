#........................................................
#   Главный модуль для проверки использования алгоритма
#   анализа изоморфных структур в графиках
#........................................................
import MetaTrader5 as mt5
import datetime
from datetime import timedelta
from netdata import netDataProcessing
from chart import chart
from compare import compare

# ******************** задание ********************
mt5.initialize()
#   pair = "EURUSD"
pair = "ETHUSD"
timeframe = "h4"
#timeframe = "d1"
chart_width = 60

start_point = datetime.datetime.now()
#start_point = ttime(2021,3,1,9,0,0)
#print(start_point)

# график
work_chrt = chart(timeframe,chart_width)
nd = netDataProcessing(pair)
# добавление графика в объект обработки данных из сети
nd.chart_add(work_chrt)
nd.do()
#work_chrt.chart_plot()
#raise SystemExit

comp = compare()
t1 = start_point
while(True):
    if(timeframe == 'h4'):
        t1 = t1 + timedelta(hours=-(chart_width*2-20))
        sample_chrt = chart(timeframe,chart_width)
        nd2 = netDataProcessing(pair,t1)
        nd2.chart_add(sample_chrt)
        nd2.do()
#        ans = comp.do_close(work_chrt,sample_chrt) # 8
#        ans = comp.do_high(work_chrt,sample_chrt) # 7
#        ans = comp.do_low(work_chrt,sample_chrt) # 7
        ans = comp.do_highlow(work_chrt,sample_chrt) # 4
#        ans = comp.do_openhigh(work_chrt,sample_chrt) # 4
        print(t1,ans)
        if(ans['q'] == 7):
            print(t1,ans)
#            work_chrt.part_plot(ans['q'],0)
            print(ans['ind'],ans['q'])
            sample_chrt.part_plot(ans['ind'],ans['ind']-ans['q'])
            raise SystemExit
#            sample_chrt.chart_plot()
#        if(ans > 6):
#            work_chrt.chart_plot()
#            sample_chrt.chart_plot()
#            print(start_point)
#            print(t1)
#            work_chrt.chart_plot()
#            sample_chrt.chart_plot()
#            print("ans=",ans)
#            work_chrt.chart_iso(ans-1)
#            sample_chrt.chart_iso(ans-1)
#            break
#        else:
#            print(t1," : ",ans)
#            pass
    
    if(timeframe == 'd1'):
        t1 = t1 + timedelta(days=-(chart_width/2+10))
        sample_chrt = chart(timeframe,chart_width)
        nd2 = netDataProcessing(pair,t1)
        nd2.chart_add(sample_chrt)
        nd2.do()
        ans = comp.do(work_chrt,sample_chrt)
        if(ans > 7):
            work_chrt.chart_iso(ans)            
            break
        else:
            pass
    if(timeframe == 'h1'):
        t1 = t1 + timedelta(hours=-(chart_width/2))
    if(timeframe == 'm30'):
        t1 = t1 + timedelta(minutes=-(chart_width*30/2))
    if(timeframe == 'm15'):
        t1 = t1 + timedelta(minutes=-(chart_width*15/2))
    if(timeframe == 'm5'):
        t1 = t1 + timedelta(minutes=-(chart_width*5/2))
    if(timeframe == 'm1'):
        t1 = t1 + timedelta(minutes=-(chart_width/2))

raise SystemExit