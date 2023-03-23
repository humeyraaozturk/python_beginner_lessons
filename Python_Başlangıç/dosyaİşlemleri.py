"""
file = open("D:\\xyz\\depo.txt","r",encoding = "UTF-8")

result = file.read()
result2 = file.readline()
#İlk satırı yazdırır.
result3 = file.readlines()
#Köşeli parantes içinde istenen satır parametresini yazdırır

"""
"""
d = input("Dosyaya Yazdırılacak Metin Giriniz: ")
file = open("D:\\xyz\\depo.txt","a",encoding = "UTF-8")
file.write(f"\n{d}")
"""
x = int(input("Kaç Adet Ürün Gireceksiniz?: "))
y = 1
z = input("Yazınız: ")

file = open("D:\\xyz\\depo.txt","w",encoding = "UTF-8")
file.write(z)

file.close()

while y<x:
    p = input("Yazınız: ")
    file = open("D:\\xyz\\depo.txt","a",encoding = "UTF-8")
    file.write(f"\n{p}")
    file.close()
    y += 1
    
