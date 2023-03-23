print("Sisteme Kaydolma \n")

sistem_güvenlik_kodu = "1234"

ka = input("Kullanıcı Adı : ")
p1 = input("Parola Belirleyiniz : ")
p2 = input("Parolayı Tekrar Yazınız : ")

if p1 == p2:
    print("Parola Doğru")
    p = p1
else :
    print("Yanlış Parola")
    print("Otomatik Parola Atandı, PAROLANIZ = 1503")
    p = "1503"
    
e_posta = input("E Posta : ")
güvenlik_kodu = input("Güvenlik Kodu : ")
if güvenlik_kodu == sistem_güvenlik_kodu :
        print("Sisteme Giriş Yapınız")
else :
        print("Güvenlik Kodu Yanlış \n\n")
        input("Tekrar Giriniz : ")
        
print("Sisteme Giriş \n")

kullanıcı_adı = input("Kullanıcı Adı : ")
parola = input("Parola : ")

if kullanıcı_adı == ka and parola == p:
    print("Hoşgeldiniz by : ", kullanıcı_adı)
elif kullanıcı_adı != ka and parola == p:
    print("Kullanıcı Adı Yanlış")
elif kullanıcı_adı == ka and parola != p:
    print("Parola Yanlış")
else:
    print("Yanlış Giriş")
"""
DÜZELTİLMELİ!!
 Güvenlik kodu ikinci kez yanlış girildiğinde sisteme giriş aşamasına geçiyor.
 Kullanıcı adı yada şifreden biri yanlış girildiğinde 
döngü duruyor.
 O aşamada sistem tekrar başlatılmalı.
 
"""



