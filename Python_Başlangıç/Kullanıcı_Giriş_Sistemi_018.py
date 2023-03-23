"""
Kullanıcıyı kayıt etmek
Kullanıcıya kayıt bilgileri ile giriş yaptırmak
"""
sistem_güvenlik_kodu = "QW159"
while True:
    print("Kayıt İşlemi")
    güvenlik_kodu = input("Güvenlik Kodu: ")
    if güvenlik_kodu != sistem_güvenlik_kodu:
        print("Güvenlik Kodunu Yanlış Girdiniz \n Yeniden Başlatılıyor...")
        continue
    
    kullanıcı_adı = input("Kullanıcı Adı: ")
    parola1 = input("Parola: ")
    parola2 = input("Tekrar Parola Giriniz: ")
    if parola1 != parola2:
        print("Şifreler Birbirleriyle Uyuşmuyor. \n Yeniden Başlatılılıyor.")
        continue
    
    e_posta = input("E Posta: ")
    
    print("Kayıt Başarılı")
    break

sistem_kullanıcı_adı = kullanıcı_adı
sistem_parola = parola1

while True:
    print("Giriş Bölümü")
    kullanıcı_adı_giriş = input("Kullanıcı Adınız: ")
    parola_giriş = input("Parolanız: ")
    
    if (kullanıcı_adı_giriş == sistem_kullanıcı_adı) and (parola_giriş == sistem_parola):
        print("Giriş Başarılı")
        print("Hoşgeldiniz {}".format(sistem_kullanıcı_adı))
        karar = input("Sistemden Çıkmak İçin X'i Tuşlayınız. ")
        if karar == "X":
            print("Görüşürüz {}".format(sistem_kullanıcı_adı))
            break
        else:
            print("Devam Ediliyor...")
    elif(kullanıcı_adı_giriş != sistem_kullanıcı_adı) and (parola_giriş == sistem_parola):
        print("Kullanıcı Adını Yanlış Girdiniz.")
        print("Yeniden Başlatılıyor. \n")
        continue
    elif(kullanıcı_adı_giriş == sistem_kullanıcı_adı) and (parola_giriş != sistem_parola):
        print("Parolayı Yanlış Girdiniz.")
        print("Yeniden Başlatılıyor. \n")
        continue
    else:
        print("Sistemde Hata Oluştu.")





