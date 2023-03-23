print("x" in "xyz")
print("w" in "xyz")
#xyz'nin içerisinde olup olmadığına bakıyor ve true yada false yazdırıyor.

liste0 = [1,2,3,4,5]
print(1 in liste0)

araba = "araba"
print("a" in araba)
#Tırnak işaretlerine dikkat et!

liste1 = [1,2,3,4,5,6,7,8,9]
for eleman in liste1:
    print("Eleman : ", eleman)

toplam = 0
for sayı in liste1:
    toplam += sayı
    print("For Döngüsü İçindeki Toplam :", toplam)
   
print("Toplam: ",toplam)

toplam = 0
demet0 = (1,2,3,4,5,6,7,8,9)
for sayı in demet0:
    print("For Döngüsü Satırı:",sayı)
    if(sayı%2) == 0 :
        toplam += sayı
#Demetin içerisindeki çift sayıları toplar.
#print("For Döngüsü İçerisindeki Toplam:", toplam)
    
    
print("Toplam:", toplam)

sözlük = {"Anahtar Değer1": 1,"Anahtar Değer2": 2,"Anahtar Değer3": 3}
for eleman in sözlük:
    print(eleman)
for eleman in sözlük.values():
    print(eleman)
for eleman in sözlük.items():
    print(eleman)

liste2 = [ [1],[2,3],[4,5,6],[7,8,9,10] ]
liste3 = []
print(len(liste2))
for eleman in liste2:
    for sayı in eleman:
        liste3.append(sayı)
print(liste3)



































