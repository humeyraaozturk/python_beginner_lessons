liste1 = list(range(0,100))
liste2 = []

for sayı in liste1:
    sayı *= 2
    liste2.append(sayı)
    
print(liste2)

#Yukarıdaki işlemi yapmanın kısa yolu
liste3 = list(range(0,100))
liste4 = [sayı *2 for sayı in liste3]
print(liste4)

liste5 = [[1],[2,3],[4,5,6],[7,8,9,10]]
liste6 = []

for eleman in liste5:
    for sayı in eleman:
        liste6.append(sayı)
        
print(liste5)
print(liste6)

liste7 = [[1],[2,3],[4,5,6],[7,8,9,10]]
liste8 = [sayı for eleman in liste7 for sayı in eleman]
# değişken_ismi = [ atanacak_eleman döngüler veya koşullar vb.]
# değişken_ismi'nin sınıfı listedir.
print(liste8)

liste9 = list(range(0,101))
liste10 = [sayı for sayı in range(0,101) if (sayı%10) == 0]
print(liste10)







