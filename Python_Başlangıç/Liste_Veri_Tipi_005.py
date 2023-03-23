a = 10
karakter_dizisi = "Merhaba D�nya"
liste0 = ["Eleman1", "Eleman2", 5, 3.24, a]
bos_liste = []
#Listelemede k��eli paraztez kullan�l�r.

print(len(liste0))
#"len" fonksiyonu liste0'�n ka� elemanl� oldu�unu yazd�r�r.

isim = "H�meyra �zt�rk"
isim_liste = list(isim)
#"list" fonksiyonu verinin her eleman�n� ayr� olarak g�sterir.

print(isim_liste)
#Bo�luk da eleman olarak kabul edilir.

liste1 = [1,2,3,4,5,6,7,8,9]
print(liste1[0])
#S�f�r�nc� eleman� yazd�r�r.
print(liste1[5])
#Be�inci eleman� yazd�r�r.
#Programlamada s�ralama s�f�rdan ba�lar
print(liste1[0:5])
#S�f�rdan be�e kadar olan elemanlar� be�inci hari� olarak yazd�r�r.
print(liste1[0:5:2])
#S�f�rdan be�e kadar olan elemanlar� iki�er atlayarak yazd�r�r.
print(liste1[ : :2])
#Ba�tan sona kadar olan elemanlar� iki�er atlayarak yazd�r�r.

liste2 = [0,1,2,3,4,5]
liste3 = [6,7,8,9]

print(liste2 + liste3)
#�ki listeyi birle�tirir.

print(liste2 * 3)
#�� kez liste2'yi yazd�r�r.

liste2.append(6)
#liste2'ye "6" eleman�n� ekler.

print("�ncesi:", liste2)
liste2.append("H�meyra")
x = "Merhaba D�nya"
liste2.append(x)
print("Sonras�: ", liste2)

liste2.pop()
print("Bir Sonraki: ", liste2)
#Eklenen son eleman� listeden ��kart�r

liste2.pop(6)
print("Bir Sonraki: ", liste2)
#Alt�nc� eleman� listeden ��kart�r.

liste2.append(liste3)
print("Daha Sonraki: ", liste2)
#Bu �ekilde yap�ld���nda "liste3" tek eleman olarak g�z�k�r.

liste4 = [1,2,3,4,5]
liste5 = [6,7,8]
liste6 = [9,10,11,12]

liste4.append(liste5)
liste4.append(liste6)

print(liste4)
print(liste4[6][1])
#liste4'�n alt�nc� eleman�n�n birinci eleman�n� �a��r�r.




























