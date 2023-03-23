yaş = int(input("Yaşınız kaç? : "))

if(yaş<18) :
    print("Yaşınız yetmiyor")
    yıl = 18-yaş
    print("{} Yıl Sonra Geliniz".format(yıl))
    
else:
    print("Hoşgeldiniz")