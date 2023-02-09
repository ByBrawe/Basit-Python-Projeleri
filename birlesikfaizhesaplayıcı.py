
import time

# ----------------------------------------------------------------------------------------------
print("Birleşik Faiz Hesaplayıcı")
print("Başlatılıyor .")
time.sleep(0.2)
print("Başlatılıyor ..")
time.sleep(0.2)
print("Başlatılıyor ...")
time.sleep(0.2)
print("Başlatılıyor ....")
time.sleep(0.2)
print("...")
time.sleep(0.2)
print("...")
time.sleep(0.2)
print("...")
time.sleep(0.2)
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")
print("...")

print("Hoşgeldiniz.")

print("İpucular:")
print("----------------------------------------------------      ------------------------------------------\nGünlük faiz için tek sayı kullanabilirsiniz \nAylık içinde örneğin 6 ay ise günlük kısmına 6 yazabilirsiniz\nYıllık içinse mantık aynıdır. 5 yıl için hesaplamak isterseniz, günlük kısmına 5 yazmanız yeterlidir \n---------------------------------------------------------------------------------------------- ") 


para= int(input("Kaç TL yatıracaksınız: "))
faiz = int(input("Faiz oranı: "))
day = int(input("Kaç gün: "))



i = 0
sonuc = 0
denklem = 0
x = 0
sonuc2 = 0

yenipara= para

while True:

    i += 1

    
    denklem = ((para)*(100+faiz))/100
    
    sonuc2 = denklem - para
    para += sonuc2
    sonuc += sonuc2

    print("{} gününde {} TL'dir.".format(i,sonuc+yenipara))  
    if i == day:
        break
    



print("faiz kazancı ", sonuc)
print("{} günde Kazanacağınız para miktarı {} TL'dir.".format(day,sonuc+yenipara))    
