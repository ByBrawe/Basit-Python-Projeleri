import json
import requests as r

dollar = float(input("Kaç dolar bozduracaksınız: "))


veri = r.get("https://api.exchangeratesapi.io/latest?base=USD")

veri = json.loads(veri.text)

usdtotry = float(veri["rates"]["TRY"])


sonuc = dollar * usdtotry


print("Dolar kuru: {} TRY".format(usdtotry))
print("{} dollarınıza göre try karşılığı:{} TRY".format(dollar,sonuc))
