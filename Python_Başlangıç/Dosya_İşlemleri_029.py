"""

open("Dosya/Yolunu/Alıyor/Deneme.txt","dosya_kipi",karakter_biçimi)

Dosya Kipleri:
    w => Yazma işlemlerinde kullanılır. Önceki bilgiler silinir.
    a => Yeni bilgileri dosyanın sonuna ekler.
    r => Okuma işlemlerinde kullanılır. Silme,ekleme vb. yapılmaz.
    r+ => Hem okuma hem yazma işlemi yapılır.

"""

dosya = open("humeyra.txt","w")

dosya.write("Merhaba Dünya :) \n")
dosya.write("Hello World \n")

#dosyamız çalışmakta olduğu için kapatmadan silemeyiz.
dosya.close()

dosya = open("humeyra.txt","a")

ekleme = "Merhabalar \n"
dosya.write(ekleme)
dosya.close()







