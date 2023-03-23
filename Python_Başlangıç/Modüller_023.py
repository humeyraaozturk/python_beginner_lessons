"""
    MODÜLLER
    Bir modülü kod satırları içerisine yükleyerek modül içerisindeki tüm
fonksiyonlar ve sınıflar kullanılabilir hale gelir.

    MODÜL KULLANIMI
    import kütüphane_adı
    # Tüm kütüphaneyi çeker
    
    from kütüphane_adı import fonksiyon1, fonksiyon2
    # Kütüphanenin sadece istenilen kısmını çeker
    
    import kütüphane_adı as ka
    # kütüphane_adı'na ka lakabını takar ve kütüphaneyi kullanacağımız zaman
    bize kolaylık sağlar.
    
    from kütüphane_adı import *
    # Belirtilen kütüphanenin içindeki her şeyi çeker.
    
    from kütüphane_adı.sınıf_adı import *
    # Kütüphanenin içindeki belirtilen sınıfın içindeki her şeyi çeker.
    
"""

import math

"""
print(dir(math))
# dir => Bilgi verir.

print(help(math))
# help => Açıklamalı olarak bize yardım eder.

print(help(math.floor))
# Sadece floor kütüphanesinin açıklaması gelir.

"""

çıktı = print(math.factorial(5))
# 5'in faktöriyelini hesaplar.

print(math.ceil(3.1))
# Kendisinden büyük en küçük tam sayıya yuvarlar.

print(math.floor(3.9)) 
# Kendisinden küçük en büyük tam sayıya yuvarlar.

from math import ceil,factorial
# Kütüphaenin sadece belirtilen iki fonksiyonu çağırılır.
# Bu iki fonksiyon dışında fonksiyon kullanılırsa hata alınır.

print(ceil(3.1))
# Kütüphaneyi 'from math import ceil,factorial' şeklinde tanımladığımızda
#'print(math.ceil(3.1))'şeklinde yazamayız. 

def factorial(sayı):
    faktöriyel = 1
    
    for x in range(1, sayı + 1): 
    #Birden başlayarak sayıya kadar gidip son sayıyı almadığı için sayı + 1 yazılır.
        faktöriyel *= x
        
    print("{}! = {} ".format(sayı, faktöriyel))
    return faktöriyel

çıktı2 = factorial(5)
# math kütüphanesinde factorial fonksiyonu olmasına ve onu çekmemize rağmen
# eğer biz ayrı olarak factorial fonksiyonu yazdıysak program bizim yazdığımız 
# fonksiyonu kullanır.


