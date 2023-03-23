#Break => Döngüyü sonlandırır.
print("HESAP MAKİNESİ V1")

while (True):
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
        
    karar2 = input("Devam Etmek İster Misiniz? (Hayır için X'i tuşlayınız.) => ")
    if karar2 == "X":
        print("Görüşürüz :)")
        break
    else:
        print("Yeniden Başlatılıyor...\n")
        
        
#Continue => Döngüyü yeniden başlatır.
"""
for sayı in range(0,100):
    if (sayı % 2) == 0:
        print("Sayı: ",sayı)
        continue
    else:
        continue
    print("Tek Sayı",sayı)
"""

sayaç = 0
while (sayaç < 10):
    if (sayaç == 5) or (sayaç == 7):
        print("Değer:",sayaç)
        sayaç += 1
        continue
    else:
        sayaç += 1
        continue
        
    print(sayı)
