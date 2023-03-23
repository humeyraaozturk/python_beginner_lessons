import time
import random

print("Sayı Tahmin Oyunu V1")
print("1-100 Arasında Bir Sayı Tutunuz")
rastgele_sayı = random.randint(1,100)
tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmininiz: "))
    
    if tahmin == rastgele_sayı:
        time.sleep(2)
        print("Tebrikler! Bildiniz..")
        print("Rastgele Sayı: ",rastgele_sayı)
        break
    
    elif tahmin > rastgele_sayı:
        time.sleep(2)
        print("Daha Küçük Bir Sayı Tutmalısın")
        print("Yeniden Dene")
        tahmin_hakkı -= 1
    
    else:
        time.sleep(2)
        print("Daha Büyük Bir Sayı Tutmalısın")
        print("Yeniden Dene")
        tahmin_hakkı -= 1
        
    if tahmin_hakkı == 0:
        time.sleep(2)
        print("Deneme Hakkınız Bitti")
        print("Rastgele Sayı: ",rastgele_sayı)
        break 