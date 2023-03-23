"""
Hata Türleri:
    Geliştirici Hataları (Söz Dizimi Hataları)
    Mantık Hataları (Formül, Hesaplama Hataları)
    İstisnalar (Kullanıcı Kaynaklı Hatalar)
    
try:
    hata ile karşılaşabileceğimiz yerler
    
except:
    hataya göre çalışacak kodlar

finally:
    hata olsun veya olmasın yapılacak işlemler

Not: Try kullanıyorsak except kullanmak zorundayız.
    
"""

print("Hesap Makinesi V1")
while True:
    try:
        x = int(input("Bir Tam Sayı Giriniz: "))
        y = int(input("Bir Tam Sayı Giriniz: "))
    except ValueError as açıklama1:
        print("Hata Oluştu :(")
        print("Hata: ",açıklama1)
        print("Program Tekrar Başlatılıyor")
        continue
    
    print("Toplama => 1")
    print("Çıkarma => 2")
    print("Çarpma => 3")
    print("Bölme => 4")
    karar = input("Yapmak İstediğiniz İşlemi Seçiniz:")
    
    try:
        if karar == "1":
            print("Toplama Yapılıyor..")
            print("Sonuç: ",(x+y))
        
        elif karar == "2":
            print("Çıkarma Yapılıyor..")
            print("Sonuç: ",(x-y))
        
        elif karar == "3":
            print("Çarpma Yapılıyor..")
            print("Sonuç: ",(x*y))
        
        elif karar == "4":
            print("Bölme Yapılıyor..")
            print("Sonuç: ",(x/y))
        
        else:
            print("Yanlış Tuşlama")
            print("Tekrar Tuşlayınız")
            continue
    except ZeroDivisionError as açıklama2:
        print("Hata Oluştu :(")
        print("Hata: ",açıklama2)
        print("Program Tekrar Başlatılıyor")
        continue
    
    
    finally:
        print("Her Hatada Çalışacak")
        
    karar2 = input("Çıkmak İçin X'i Devam Etmek İçin Herhangi Bir Tuşu Tuşlayınız")
    
    if karar2 == "X":
        print("Hoşçakalın..")
        break
    else:
        print("Yeniden Başlatılıyor...")
        continue
    
    
    
    
    