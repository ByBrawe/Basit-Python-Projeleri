

print("ŞEN".ljust(20) + "Hesap Makinesi \ntoplama=1\nçıkarma=2\nçarpma=3\nbölme=4")
islem = input("Hangi işlemi yapmak istiyorsanız: ")
ilksayi = int(input("Birinci Sayiyı Giriniz: "))
ikincisayi = int(input("Bir İkinci Sayiyı Giriniz: "))


if islem == "1":
    sonuc = ilksayi + ikincisayi
    print("Sonuç: " + str(sonuc))
elif islem == "2":
    sonuc = ilksayi - ikincisayi
    print("Sonuç: " + str(sonuc))
elif islem == "3":
    sonuc = ilksayi * ikincisayi
    print("Sonuç: " + str(sonuc))
elif islem == "4":
    sonuc = ilksayi / ikincisayi
    print("Sonuç: " + str(sonuc))
else:
    print("Hatalı değer girdiniz. Lüftfen Tekrar değer giriniz.")