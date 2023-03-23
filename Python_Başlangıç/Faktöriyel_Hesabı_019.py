"""
FAKTÖRİYEL

"""

while True:
    sayı = int(input("Bir Tam Sayı Giriniz: "))
    
    if sayı < 0:
        print("Negatif sayıların faktöriyel hesabı yapılmaz.")
        
    elif sayı == 0:
        print("Sonuç: ",1)
        
    else:
        faktöriyel = 1
        
        for x in range(1, sayı + 1): 
        #Birden başlayarak sayıya kadar gidip son sayıyı almadığı için sayı + 1 yazılır.
            faktöriyel *= x
            
        print("Sonuç: ", faktöriyel)
        
    karar = input("Sistemden Çıkmak İçin X'i Tuşlayınız. ")
    if karar == "X":
        print("Görüşürüz ")
        break
    else:
        print("Devam Ediliyor...")
            
        
        
        
        
        
        
        
        
        