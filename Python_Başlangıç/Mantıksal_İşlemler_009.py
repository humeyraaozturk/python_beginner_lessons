"""
Dersin İçeriği :
    Mantıksal Değerler => Boolean(True,False)
    Karşılaştırma Operatörleri => (> , < , >= , <= , == , !=)
    Mantıksal Bağlaçlar => (and, or, not)
"""

#MANTIKSAL DEĞERLER

doğru = True
yanlış = False

print(type(doğru))
print(type(yanlış))


#KARŞILAŞTIRMA OPERATÖRLERİ


print(5 < 10)
print(5 > 10)
print(3.24 < 5)
 
print("ALİ" == "ali")
#Büyük harf ve küçük harf hiçbir zaman birbirine eşit değildir.
print("ALİ" != "ali")
print("ALİ" > "Beyza")  # 1 > 2  #(Alfabetik sıraya göre)
print("Cemal" > "Beyza")  # 3 > 2

#MANTIKSAL BAĞLAÇLAR

print(("Cemal" > "Beyza") and ( 1 > 0 ) and ( 5 > 6 ))
#and fonksiyonunda bir adet yanlış olması sonucu yanlışa götürür.

print(("Cemal" > "Beyza") or ( 1 > 0 ) or ( 5 > 6 ))
#or fonksiyonunda bir adet doğru olması sonucu doğruya götürür.

print(not(("Cemal" > "Beyza") and ( 1 > 0 ) and ( 5 > 6 )))
#not fonksiyonu aslında false olan sonucu tersi olan true sonucuna götürür.

    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
    
    