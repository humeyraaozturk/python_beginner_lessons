import time
sayaç = 0
while(sayaç < 10):
    print(sayaç)
    sayaç += 1
"""
For döngüsünde eleman bitince işlem sonlanırken
while döngüsünde koşul sağlanana kadar döngü devam eder.
"""
liste1 = [1,2,3,4,5,6,7,8,9]
sayaç = 0
while(sayaç < len(liste1)):
    print("İndeks: ",sayaç," Değer: ",liste1[sayaç])
    sayaç += 1
    
print("Hoşgeldin :)")

while True:
#True yazdıktan sonra döndü hep çalışır.

    x = int(input("Lütfen Birinci Sayıyı Giriniz: "))
    y = int(input("Lütfen İkinci Sayıyı Giriniz: "))
    karar = input("Toplama için | +, Çıkarma için | -, Çarpmaiçin | *, Bölme için | / Tuşlayınız: ")
    
    if karar == "+":
        print("Toplama Yapılıyor...")
        time.sleep(2)
        print("Sonuç: ",x+y)
    elif karar == "-":
        print("Çıkarma Yapılıyor...")
        time.sleep(2)
        print("Sonuç: ",x-y)
    elif karar == "*":
        print("Çarpma Yapılıyor...")
        time.sleep(2)
        print("Sonuç: ",x*y)
    elif karar == "/":
        print("Bölme Yapılıyor...")
        time.sleep(2)
        print("Sonuç: ",x/y)
    else:
        print("Yanlış Tuşlama!")
""" 
    time.sleep(2)
    print("\nDevam Ediliyor...")
    NOT: Bu kısmı görmediği için yoruma alındı.
"""