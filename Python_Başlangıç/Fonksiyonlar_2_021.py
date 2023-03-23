"""
Global ve Yerel Değişkenler

Global => Fonksiyonlar dışında oluşturulmuş tüm değişkenlerdir.
Yerel => Fonksiyon içerisinde oluşturulmuş tüm değişkenlerdir.

Yerel değişkenler sadece fonksiyon içerisinde kullanılır.
İşlem bittikten sonra hafızadan silinir.

Global değişkenler her yerde kullanılabilir ve çağırılabilir.
İşlem bittikten sonra hafızadan silinmez.

"""
def balina():
    a = 100         #Yerel değişken 
    print(a)
    
balina()
# Fonksiyon çağırılır ve a değeri yazdırılır.

#print(a)  =HATA=
# a değeri fonksiyonun içinde tanımlı olduğu için hata alınır.

a = 100         #Global değişken
def mavi_balina():
    print(a)
    
mavi_balina()

b = 24
def yerel():
    b = 34
    print("Yerel Değişken: ", b)
    #Fonksiyon içinde olduğu için fonksiyonun içinde tanımlı olan b yazdırılır.
    
yerel()
print("Global Değişken: ", b)
#Globalde tanımlı olan b yazdırılır.

c = 20
def glo():
    global c        
    #c'yi fonksiyonun içinde global değer olarak atamamızı sağlar.
    #Bu işlem sayesinde globaldeki c'nin değerini de değiştirebiliriz.
    c = 40
    print("Yerel Değişken", c)
    
glo()
print("Global Değişken: ", c)
#ikisinin çıktısı aynı ve 40'dır.

"""
Lambda Fonksiyonu

fonksiyon_ismi = lambda parametre : return ifadesi

"""
# -1-
def iki_katı(x):
    return x*2

x = iki_katı(5)

# -2-
iki_katı2 = lambda x : x*2
x2 = iki_katı2(5)

# 1 ve 2 ifadeleri birbirine denktir.
# 1'i lambda kullanarak 2. ifadeyle kolayca yazabiliriz.

# -3-

def topla(x, y, z):
    return x+y+z

toplam = topla(10, 20, 30)

# -4-

topla2 = lambda x, y, z : x+y+z

# print(type(topla2))   => function

toplam2 = topla2(10, 20, 30)

# 3 ve 4 ifadeleri birbirine denktir.

# -5-
def tek_çift(x):
    if (x % 2 == 0):
        print("{} Değeri Çifttir.".format(x))
    else:
        print("{} Değeri Tektir.".format(x))

tek_çift(5)

# -6-
tek_çift2 = lambda x : (x % 2 == 0)
deger = tek_çift2(5)
#True-False değeri döndürülür.
#True => Çift | False => Tek
# 5 ve 6 ifadeleri birbirine denktir.





