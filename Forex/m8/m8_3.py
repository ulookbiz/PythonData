#IEX работает за деньги или фри через песочницу
#попытки взять данные для форекса неудачные, теряю время

import numpy as np
import pandas as pd
import requests
#import xlswriter
import math

pd.DataFrame()
#stocks = pd.read_csv('sp_500_stocks.csv')

#pk_9fe77ee1392f4ee7a638c4181da1c75e
#sk_ff1b55dac690472ebd83d2abd031b9a8

# Acquiring an API Token
IEX_CLOUD_API_TOKEN = 'pk_9fe77ee1392f4ee7a638c4181da1c75e'
#from secrets import IEX_CLOUD_API_TOKEN
symbol = 'AAPL'
#api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
#api_url = f'https://cloud.iexapis.com/stable/tops?token=sk_ff1b55dac690472ebd83d2abd031b9a8&symbols=aapl'
#api_url = f'https://cloud.iexapis.com/stable/forex/latest?token=sk_ff1b55dac690472ebd83d2abd031b9a8&symbols=usdcad'
#api_url = f'https://cloud.iexapis.com/stable/fx/latest?token=sk_ff1b55dac690472ebd83d2abd031b9a8&symbols=EURUSD'
#api_url = f'https://cloud.iexapis.com/stable/tops?token=sk_ff1b55dac690472ebd83d2abd031b9a8&symbols=usdcad'
print(api_url)
data = requests.get(api_url).json()
print(data)