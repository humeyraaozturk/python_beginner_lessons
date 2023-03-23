
mesaj = input("Mesaj: ")
print("Mesajınız: ",mesaj)
print("Mesajın Veri Türü: ",type(mesaj))

mesaj_int = int(input("Mesajınız(Sayı): "))
#int fonksiyonu olduğu için mesaj sayı olmalı.
print(mesaj_int * 3)
#girilen int olduğu için 3 ile çarpılıp yazdırılır.

print(mesaj * 3)
#İnt yada string ayırt etmez. Yazılan sayı yada harfi 3 kez yazdırır.

x = int(input("Toplanılacak Sayı Giriniz:"))
y = int(input("Toplanılacak Sayı Giriniz:"))
print("{} + {} = {}".format(x, y, x+y))
"""
Not= İnput fonksiyonunun başına int yazdığımız için girilen değer sayı harici
bir şey olduğunda program hata verecek. Eğer inputun başına int yazmasaydık 
aşağıda format parantezinin  içine int(x)+int(y) yazmamız gerekirdi.
"""





