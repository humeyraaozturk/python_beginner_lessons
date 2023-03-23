def mesaj(isim):
    print("Günaydın by" , isim)
    print("{} Nasılsın?".format(isim))

mesaj("Hümeyra")

def toplama(x, y):
    print("Sonuç" , (x+y))
    
toplama(5,8)
#Parametreye fonksiyonda belirtilenin aksine 2 den farklı sayıda
#değer girilirse hata alınır.

def topla(* parametreler):
    # *parametreler şeklinde yazıldığında istenilen sayıda değer girilebilir.
    # Alınan değerleri tuple a atar.
    print("Girilen Değerler: ", parametreler)
    toplam = 0
    for sayı in parametreler:
        toplam += sayı
    print("Sonuç: ", toplam)
    
    
topla(2,3)
topla(2,3,4,5,6)

def bilgiler(isim = "Yok", soyisim = "Yok", numara = "Yok"):
    print("Bilgiler Yazdırılıyor...")
    print("\n İsim:: {} \n Soyisim: {} \n Numara: {}".format(isim, soyisim, numara))
   
bilgiler()
bilgiler("Ünver",1)
"""
İsim:: Ünver 
Soyisim: 1 
Numara: Yok
"""
bilgiler(soyisim = "Ünver", numara = 1)
"""
İsim:: Yok 
Soyisim: Ünver 
Numara: 1
"""
bilgiler(numara = 1)
"""
İsim:: Yok 
Soyisim: Yok 
Numara: 1
"""

def iki_katı(x):
    print("1. Fonksiyon", x*2)
    return x*2

def iki_eksiği(x):
    print("2. Fonksiyon", x-2)
    return x-2

def iki_bölümü(x):
    print("3. Fonksiyon", x/2)
    return x/2

sayı = int(input("Bir tam sayı giriniz: "))
print("Sonuç: ", iki_bölümü(iki_eksiği(iki_katı(sayı))))


def işleme(a):
    print("{} Değeri İşleniyor...".format(a))
    print("{} Değerinin 2 Katı Alındı".format(a))
    print("{} Değeri İşlendi".format(a))
    print("Sonuç: ", a*2)
    return a*2

işleme(5)

























