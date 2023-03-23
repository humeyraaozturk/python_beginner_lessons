from random import choice
import pandas as pd

data  = pd.read_csv("TR_ŞEHİRLER.csv",encoding="UTF-8")

şehir_isimleri = data["BASLIK"]

rastgele_şehir = choice(şehir_isimleri)

harf_sayı = len(rastgele_şehir)

print("Tahmin Oyununa Hoşgeldiniz")

print("{} Harflidir".format(harf_sayı))

print("Şehrin İlk Harfi => {}".format(rastgele_şehir[0]))

deneme_hakkı= 3

while True:
    cevap= input("Tahmininiz:  ")
    
    if cevap.upper() == rastgele_şehir.upper():
        print(cevap.upper())
        print("Tebrikler Doğru Tahmin")
        karar= input("Oyuna Devam Etmek İster Misiniz? Hayır İçin 0/ Evet İçin 1 => ")
        if karar== "0":
            print("Hoşçakalın")
            break
            
        elif karar=="1":
            print("Bu Sefer Başarabilirsin")
            rastgele_şehir = choice(şehir_isimleri)

            harf_sayı = len(rastgele_şehir)

            print("{} Harflidir".format(harf_sayı))

            print("Şehrin İlk Harfi => {}".format(rastgele_şehir[0]))
            continue

        else:
            print("Bu Sefer Başarabilirsin")
            rastgele_şehir = choice(şehir_isimleri)
            
            harf_sayı = len(rastgele_şehir)
            
            print("{} Harflidir".format(harf_sayı))

            print("Şehrin İlk Harfi => {}".format(rastgele_şehir[0]))
            continue
    
    else:
        print("Yanlış Tahmin")
        print("{} Hakkınız Kaldı".format(deneme_hakkı))
        deneme_hakkı -=1
        if deneme_hakkı < 0:
            print("Hakkınız Bitti")
            print("Oyun Sonlandı")
            print("Doğru Tahmin: ",rastgele_şehir)
            karar= input("Oyuna Devam Etmek İster Misiniz? Hayır İçin 0/ Evet İçin 1 => ")
            if karar== "0":
                print("Hoşçakalın")
                break
                
            elif karar=="1":
                print("Bu Sefer Başarabilirsin")
                rastgele_şehir = choice(şehir_isimleri)

                harf_sayı = len(rastgele_şehir)

                print("{} Harflidir".format(harf_sayı))

                print("Şehrin İlk Harfi => {}".format(rastgele_şehir[0]))
                continue

            else:
                print("Bu Sefer Başarabilirsin")
                rastgele_şehir = choice(şehir_isimleri)

                harf_sayı = len(rastgele_şehir)
                
                print("{} Harflidir".format(harf_sayı))

                print("Şehrin İlk Harfi => {}".format(rastgele_şehir[0]))
                continue
        else:
            print("Tekrar Deneyiniz")