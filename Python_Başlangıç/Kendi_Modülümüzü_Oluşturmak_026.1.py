import Kendi_Modülüm_026
"""
Kendi modülümüzü proje dosyamızda kullanabilmemiz için 
proje dosyası ve modülün aynı klasörde olması gerekir.
"""
#print(dir(Kendi_Modülüm_026))

print("Hesap Makinesi Programı V1")

while True:
    print("Toplama => 1")
    print("Çıkarma => 2")
    print("Çarpma => 3")
    print("Bölme => 4")
    print("Kalansız Bölme => 5")
    print("Kalan Bulma => 6")
    print("Üs Alma => 7")
    karar = input("Yapmak İstediğiniz İşlemi Seçiniz:")
    
    
    x = int(input("Bir Tam Sayı Giriniz: "))
    y = int(input("Bir Tam Sayı Giriniz: "))
    
    if karar == "1":
        print("Toplama Yapılıyor..")
        print("Sonuç: ",Kendi_Modülüm_026.topla(x, y))
    
    elif karar == "2":
        print("Çıkarma Yapılıyor..")
        print("Sonuç: ",Kendi_Modülüm_026.çıkartma(x, y))
    
    elif karar == "3":
        print("Çarpma Yapılıyor..")
        print("Sonuç: ",Kendi_Modülüm_026.çarpma(x, y)) 
    
    elif karar == "4":
        print("Bölme Yapılıyor..")
        print("Sonuç: ",Kendi_Modülüm_026.bölme(x, y))
    
    elif karar == "5":
        print("Kalansız Bölme Yapılıyor..")
        print("Sonuç: ",Kendi_Modülüm_026.kalansız_bölme(x, y))
    
    elif karar == "6":
        print("Kalan Bulma Yapılıyor..")
        print("Sonuç: ",Kendi_Modülüm_026.kalan(x, y))
    
    elif karar == "7":
        print("Üs Alma Yapılıyor..")
        print("Sonuç: ",Kendi_Modülüm_026.üs_alma(x, y))
    
    else:
        print("Yanlış Tuşlama")
        print("Lütfen Tekrar Tuşlayınız..")
        continue
    
    karar2 = input("Çıkmak İçin X'i Devam Etmek İçin Herhangi Bir Tuşu Tuşlayınız")
    
    if karar2 == "X":
        print("Hoşçakalın..")
        break
    else:
        print("Yeniden Başlatılıyor...")
        continue
