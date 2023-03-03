# Компиляция файла G:\PythonData\Forex\m8\m8_2.py
#   G:
#   cd pyinstaller
#   pyinstaller G:\PythonData\Forex\m8\m8_2.py -F
#
import tkinter as tk
from tkinter import ttk

class winApp(tk.Tk):
#......................................
# Исходные данные и формирование окна
    def __init__(self):

        super().__init__()

#       задание исходных данных
        self.pairs = ['EURUSD','GBPUSD','USDJPY','XAUUSD','GBPCAD']
        self.moves = ['up','down']
        self.lines = ['bid','ask']

#       выходные данные
        self.rpair = []
        self.rprice = []
        self.rmove = []
        self.rline = []

#       промежуточные необработанные данные
        self.pair_entry = []
        self.price_entry = []
        self.dir_entry = []
        
#       создание окна ввода
        self.geometry("600x375")
        self.title('Наблюдение за курсами валют')
        self.resizable(0, 0)

#       configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        self.create_widgets()
        
#......................................
# Формирвание результат после нажатия кнопки
    def butt(self):
        
        for i in range(5):
#            print(self.pair_entry[i].get())
            if self.pair_entry[i].get() in self.pairs:
                if self.dir_entry[i].get() in self.moves:
                    if self.price_entry[i].get().isdigit() == True:
                        self.rpair.append(self.pair_entry[i].get())
                        self.rprice.append(self.price_entry[i].get())
                        self.rmove.append(self.dir_entry[i].get())
                        if(self.dir_entry[i].get() == 'up'):
                            self.rline.append('bid')
                        else:
                            self.rline.append('ask')
                            
#        for pe in self.pair_entry:
#            print(pe.get())
#        for pe in self.price_entry:
#            print(pe.get())
#        for pe in self.dir_entry:
#            print(pe.get())

        tk.Tk.destroy(self)

#......................................
# Возврат массива определившихся пар 
    def getpairs(self):

        return self.rpair

#......................................
# Возврат массива определившихся уровней-заданий
    def getlevels(self):

        leng = len(self.rpair)
        ret = []
        for i in range(leng):
            ready = dict()
            ready[self.rpair[i]] = self.rprice[i]
            if(self.rmove[i] == 'up'):
                ready['move'] = '+'
            else:
                ready['move'] = '-'
            ready['line'] = self.rline[i]
            ret.append(ready)

        return ret

#......................................
    def create_widgets(self):
        # pair
        pair_label = ttk.Label(self, text="Валютная пара:")
        pair_label.grid(column=1, row=0, sticky=tk.NS, padx=5, pady=15)

        # price
        price_label = ttk.Label(self, text="Контрольная цена:")
        price_label.grid(column=2, row=0, sticky=tk.NS, padx=5, pady=15)

        # direction
        dir_label = ttk.Label(self, text="При движении:")
        dir_label.grid(column=3, row=0, sticky=tk.NS, padx=5, pady=15)

        for i in range(5):
            self.pair_entry.append(ttk.Entry(self))
            self.pair_entry[i].grid(column=1, row=i+1, sticky=tk.NS, padx=5, pady=15)

            self.price_entry.append(ttk.Entry(self))
            self.price_entry[i].grid(column=2, row=i+1, sticky=tk.NS, padx=5, pady=15)

            self.dir_entry.append(ttk.Entry(self))
            self.dir_entry[i].grid(column=3, row=i+1, sticky=tk.NS, padx=5, pady=15)

        # start button
        start_button = ttk.Button(self, text="Пуск", command = self.butt)
        start_button.grid(column=3, row=6, sticky=tk.NS, padx=10, pady=15)

#if __name__ == "__main__":
#    app = App()
#    app.mainloop()
