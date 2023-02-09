import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate



veri = requests.get("https://web-api.coinmarketcap.com/v1/cryptocurrency/market-pairs/latest?slug=bitcoin&start=1&limit=100&convert=USD&category=spot&sort=market_reputation&aux=num_market_pairs,category,market_url,notice,price_quote,effective_liquidity,market_score,market_reputation").text

ayirma = json.loads(veri)

re = ayirma['data']["market_pairs"]

# exchange = re[0]["exchange"]["slug"]
# market_pair = re[0]["market_pair"]
# quote = re[0]["quote"]["exchange_reported"]["price"]

# print("Borsa".ljust(20) + " Parametre".ljust(22) + "Fiyat")

deneme = []
for i in re:
    if i["market_pair"] == "BTC/USDT":
        exchange = i["exchange"]["slug"]
        market_pair = i["market_pair"]
        quote = i["quote"]["USD"]["price"]
        # print(f'{exchange.ljust(20)} {market_pair.ljust(20)} {round(quote,2)}')
        deneme.append([exchange,market_pair,quote])

df = pd.DataFrame(deneme,columns=["Borsa","Parametre","Fiyat"]).sort_values(by="Fiyat", ascending=False)

# print("#####Büyükten küçüğe sıralanmış tablo####")
print(tabulate(df,headers='keys', tablefmt='psql'))
# print(df.to_markdown())
#print(df.to_json(orient="table"))


max_borsa = df['Borsa'].tail(1).values[0]
min_borsa = df['Borsa'].head(1).values[0]

# Yedek
#max_borsa1 = df.loc[df['Fiyat'].idxmin(),'Borsa']
#min_borsa2 = df.loc[df['Fiyat'].idxmax(),'Borsa']

min_price = df['Fiyat'].min()
max_price = df['Fiyat'].max()

degisim = round(((max_price-min_price)/max_price)*100,2)




print("\nMinumum Fiyat")
print(tabulate(df.tail(1),headers='keys', tablefmt='psql'))
print("\nMaksimum Fiyat")
print(tabulate(df.head(1),headers='keys', tablefmt='psql'))

print()


hesap = (10000*degisim)


print(f"{max_borsa} -> {min_borsa} borsasına transfer etmen gerekiyor")
print(f"Fiyat farkı = {round(max_price-min_price,2)} USDT")
print(f"% {degisim} oranında kar edebilirsin")

print(f"\nBonus \n10 bin dolarda kaç para kazanacaksın: {(10000/min_price)*max_price*degisim/100} USDT")
print(f"bin dolarda kaç para kazancaksın: {(1000/min_price)*max_price*degisim/100} USDT")
print(f"500 dolarda kaç para kazancaksın: {(500/min_price)*max_price*degisim/100} USDT")
print(f"250 dolarda kaç para kazancaksın: {(250/min_price)*max_price*degisim/100} USDT")

print("\n------------------")



input("Kapatmak için Enter Tuşuna bas")










