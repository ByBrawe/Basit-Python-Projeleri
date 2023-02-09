##fake mail adres oluşturma denemesi

import random
import string



# soru = int(input("Kaç tane mail oluşturmak istiyorsun?: "))
mailuzanti = ["gmail.com","yandex.com","hotmail.com","yahoo.com","outlook.com","mynet.com"]


# mail uzantı rastgele oluşturmak
# mailuzanti[random.randint(0,5)]

liste = ""

isimler="""uncommonecdysiast
daresshovels
bouncecloths
chumpjeremiah
wattcopper
datagenes
professionalbrittle
bakingfish
signorratty
languidcedar
newtonshammock
churncoledale
buckwildfire
depravitythorley
ceepsuggests
glagboberts
foodsale
wobblinesserring
repairlope
wickhamester
brokenlayla
vestturnips
pollenhole
otterusual"""

def karisiksayiuret(x):
    return ''.join(random.choice(string.ascii_letters) for y in range(x))

def karisikuret(x):
    return ''.join(random.choice(string.digits) for y in range(x))



isimlist= isimler.split("\n")

## for'un farklı kullanımına bak

##yenilist = []
##
##for x in isimlist:
##    yenilist.append(x[1])
##print(*yenilist, sep="")    

for x in isimlist:
    liste += x
    liste += karisikuret(random.randint(2,5))
    liste += "@"
    liste += random.choice(mailuzanti)
    liste += ":" + karisiksayiuret(random.randint(6,12))
    liste += "\n"

#dosya işlemleri

dosya = open("mail.txt","a")
dosya.write(liste),
dosya.close()

    

print(liste)    

    













