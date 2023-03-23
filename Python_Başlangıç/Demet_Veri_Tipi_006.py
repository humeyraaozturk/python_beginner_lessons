a = 10
liste = [[1,2], [3,4]]
demet = ("Eleman1", "Eleman2", 5, 5.24, a, [1,2,3], liste)
print(demet)

"""
tek_elemanlı_demet = (5)
Bu şekilde yazıldığında sistem bunu integer olarak algılar.
"""
tek_elemanlı_demet = (5,)
#Bu şekilde tuple olarak algılar ve tek elemanlı olur.

liste2 = ["Eleman1",5,3.24]
demet2 = ("Eleman1",5,3.24)

print("Önceki:", liste2)
print("Önceki:", demet2)

liste2[0] = 7
#liste2'deki sıfırıncı indeksi '7' ile değiştirir.
print("Sonraki:", liste2)

"""
demet2[0] = 7
print("Sonraki:", demet2)
 => Yapıldığında SyntaxError verir çünkü demetler değiştirilemez.

 !!! LİSTELER DEĞİŞTİRİLEBİLİRKEN DEMETLER DEĞİŞTİRİLEMEZ!!!
"""

print(demet2.index("Eleman1"))
#demet2'deki "Eleman1" isimli elemanın indeksini yazdırır.

demet3 = (1,1,1,1,3,3,5,5,5,5,5,5,7,7,8,9)
print(demet3.count(5))
#demet3'teki '5' elemanının kaç kere tekrar ettiğini yazdırır.

#Demetler "()" ile ifade edilirken listeler "[]" ile ifade edilir.



















