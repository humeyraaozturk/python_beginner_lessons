from random import choice
import time

değerler = ["taş","kağıt","makas"]

while True:
    print("\nTaş Kağıt Makas Oyununa Hoşgeldiniz :)")
    
    kullanıcı = str(input("Taş mı?, Kağıt mı?, Makas mı? =>"))
    
    kullanıcı = kullanıcı.lower()
    print("Sizin Seçiminiz: ",kullanıcı)
    
    bilgisayar = choice(değerler)
    print("Bilgisayarın Seçimi: ",bilgisayar)

    if kullanıcı == "taş":
        if bilgisayar == "taş":
            print("Durum Berabere")
        elif bilgisayar == "kağıt":
            print("Üzgünüz Kaybettiniz :(")
        elif bilgisayar == "makas":
            print("Tebrikler Kazandınız")
            
    elif kullanıcı == "makas":
        if bilgisayar == "taş":
            print("Üzgünüz Kaybettiniz :(")
        elif bilgisayar == "kağıt":
            print("Tebrikler Kazandınız")
        elif bilgisayar == "makas":
            print("Durum Berabere")
        
    elif kullanıcı == "kağıt":
        if bilgisayar == "taş":
            print("Tebrikler Kazandınız")
        elif bilgisayar == "kağıt":
            print("Durum Berabere")
        elif bilgisayar == "makas":
            print("Üzgünüz Kaybettiniz :(")
        
    else:
        print("Yanlış Seçim")
        
    print("Oyuna Devam Etmek İster Misiniz? ")
    karar = input("Evet = 1/Hayır = 0 => ")
    if karar == "Hayır" or karar == "hayır" or karar == "HAYIR" or karar == "0":
        print("Görüşmek Üzere..")
        break
    else:
        print("Yeniden Başlatılıyor")
        time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    