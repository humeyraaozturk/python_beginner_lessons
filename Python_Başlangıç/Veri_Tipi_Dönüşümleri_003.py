ondalık_sayı = 3.24
tam_sayı = 542
karakter_dizi1 = 542
karakter_dizi2 = 542.2424
karakter_dizi3 = 542344.24

"""
  => Tam sayıya çevirmek için "int" kullanılır.
  => Ondalıklı sayıya çevirmek için "float" kullanılır.
  => "ValueError" değer hatası demektir.
"""

print(float(tam_sayı))
#Sayıyı ondalıklı sayıya çevirmek için kullanılır.

print(int(ondalık_sayı))
#Sayının tam kısmını göstermek için kullanılır.

print(type(karakter_dizi1))
#Sayının tipini göstermek için kullanılır.

karakter_dizi3 = int(karakter_dizi3)
#Sayının tipini floattan int e çevirmek için kullanılabilir.

print(type(karakter_dizi3))


