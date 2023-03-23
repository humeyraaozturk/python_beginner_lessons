print("HESAP MAKİNESİ V1")

x = int(input("Birinci Sayıyı Giriniz : "))
y = int(input("İkinci Sayıyı Giriniz : "))
z = x+y

print("Yapılacak İşlemi Seçiniz;")
print("Toplama İçin + | Çıkarma İçin - | Çarpma İçin * | Bölme İçin / ")
karar = input("İşlem Türü: ")

if (karar == "+"):
    print("Toplama Yapılıyor")
    print("Sonuç : ", x+y)
    
elif (karar == "-") :
    print("Çıkarma Yapılıyor")
    print("Sonuç : ", x-y)

elif (karar == "*") :
    print("Çarpma Yapılıyor")
    print("Sonuç : ", x*y)

    
elif (karar == "/") :
    print("Bölme Yapılıyor")
    print("Sonuç : ", x/y)

    
else :
    print("Yanlış Tuşlama")

