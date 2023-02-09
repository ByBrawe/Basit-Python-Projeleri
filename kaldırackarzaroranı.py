
# kaldıraç sistemine göre kar zarar oranı

para = int(input("Kaç lira yatıracaksınız: "))
kaldirac = int(input("Kaldıraç oranı: "))
yuz = int(input("yüzde kaç oranında yükselince kar edersin hesabı: "))

miktar = (para*kaldirac)

x = 100/kaldirac

kar = para + miktar*(yuz)/100
zarar = para - miktar*(yuz)/100



print("-------------------------\n\n")
print("{} kaldıraç oranı ile toplam işlem yapacağınız para miktar: {}".format(kaldirac,miktar))
print("Satın aldığınız coin, %{} oranında düştüğünde paranızın tamamını kaybedersiniz".format(x))

print("{} oranında yükselişte toplam para: {}".format(yuz,kar))
print("{} oranında düşüşte net kalan para: {}".format(yuz,zarar))
