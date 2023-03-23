liste1 = list(range(0,100))
print(liste1)
#range fonksiyonu burada 0'dan 100'e kadar olan(100 hariç) değerleri yazdırmak için kullanılır.
#Başına list yazarak range fonksiyonundan gelen verileri liste tipine dönüştürürüz.
demet1 = tuple(range(0,100))
#tuple demet demektir.Burada oluşturulan range fonksiyonu demet veri tipine dönüştürülür.
print(demet1)
print(*demet1)
#'*' her bir elemanı ayrı bir string olarak incelemeye yarar.
print(*range(0,100,10))
#0'dan 100'e kadar 10'ar atlayarak gider.
print(* range(100,0,-1))
#100'den 0' a kadar normalde gidemez 
#ama bu şekilde yazınca 1'er azalarak git demiş oluyoruz.
yeni_liste = list()
for sayı in range(0,100):
    sayı*=2
    yeni_liste.append(sayı)
    print(yeni_liste)



