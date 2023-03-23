def asal(x):
    while True:
        if x < 0:
            print("{} değeri Asal Değildir.".format(x))
            break
        
        sayaç = 0
        for sayı in range(2, x):
            if (x % sayı == 0):
                sayaç += 1
        if sayaç != 0:
            print("{} Değeri Asal Değildir. ".format(x))
            break
        
        else: 
            print("{} Değeri Asaldır".format(x))
            break

x = int(input("Bir Tam Sayı Giriniz: "))        
asal(x)


"""

Bir Sayının Tam Sayı Bölenlerini Bulan Fonksiyon

"""

def tam_sayı_bölenleri(y):
    bölenler = []
    for sayı2 in range(1, x+1):
        if (x % sayı2  == 0):
            bölenler.append(sayı2)
            
    print("Tam Bölenler Listesi: ", bölenler)
    return bölenler
    
y = int(input("Bir Tam Sayı Giriniz: "))
bölenler_listesi = tam_sayı_bölenleri(y)



























