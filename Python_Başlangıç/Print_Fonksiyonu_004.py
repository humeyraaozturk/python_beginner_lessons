print(35+35) 
print("35+35")
print("35" + "35")

isim = "Hümeyra"
print(* isim)
#Mesajın her bir elemanını ayrı bir string olarak inceler.

print("İsminiz:", isim) 
print("İsminiz: \t", isim)
#Bir tab boşluğu bırakarak yazdırır.

print("10", "10", "2010",sep=("/"))
#Sep ile ifade edilen simgeyi sıralı elemanlar arasına koyarak yazdırır.

a = 5
b = 10
print("{} + {} = {}".format(a, b, a+b))
#Format ile ifade edilenleri sırasıyla {} içine koyarak işlem yapar ve sonucu yazdırır.

x = input("Toplanılacak sayı giriniz => ")
y = input("Toplanılacak sayı giriniz => ")
print("{} + {} = {}".format(x, y, int(x) + int(y)))
#Kullanıcının girdiği ifadelere göre işlem yapar ve yazdırır.