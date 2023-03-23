sözlük_ismi = {"Anahtar_Veri":"Değer"}
"""
Aynen sözlüklerde olduğu gibi. Her anahtar verinin bir değer karşılığı var.
Buradaki değeri çağırmak için sıfırıncı indeksi çağırmayacağız.
Sözlük isminden anahtar veriyi print ettiğimizde değeri çağırmış olacağız.

"""
print(sözlük_ismi["Anahtar_Veri"])

sözlük1 = {"Bir": 1, "İki":[1,2,3], "Üç":[[1,2], [3,4], [5,6]], "Dört": 24}
sözlük1["Anahtar Veri"] = "Merhaba Dünya"
print(sözlük1)
#Bu şekilde sözlük1'in içine "Anahtar Veri"yi ve değerini eklemiş olduk.

print(sözlük1["Üç"][2][1])
#Sözlük1'in içindeki "Üç" değerinin ikinci indeksinin birinci indeksini yazdırır.

boş_sözlük = {}

iç_içe_sözlük = {"Birden Beşe":{"Bir":1, "İki":2, "Üç":3, "Dört":4, "Beş":5}}
print(iç_içe_sözlük["Birden Beşe"]["Dört"])
#Bu şekilde "Dört" elemanına atanan değeri öğreniriz.

print(iç_içe_sözlük.values())
#Anahtar sözcüğün değerini yazdırır.

print(iç_içe_sözlük.keys())
#Anahtar sözcüğü yazdırır.

print(iç_içe_sözlük.items())
#Aynı anda hem anahtar veriyi hem de değeri yazdırır.








