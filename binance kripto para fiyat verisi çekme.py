import requests
import json
import pandas as pd

market = 'AVAXUSDT'
tick_interval = '1h'
url = 'https://api.binance.com/api/v3/klines?symbol='+market+'&interval='+tick_interval
get = requests.get(url)
data = get.json()

veriler = []
pd.set_option('display.max_rows', 1000)
for i in data:

    veriler.append([i[0],i[2],[3]])
tablo = pd.DataFrame(veriler, columns=["Veri1","Veri2","Veri3"])
tablo.to_excel("output.xlsx")

print(tablo)