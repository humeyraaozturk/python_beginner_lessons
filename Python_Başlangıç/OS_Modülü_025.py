"""
Os Modülü => Dosya ve klasör işlemlerinde bizlere yardımcı olur.
"""

import os
klasorYolu = os.getcwd()
#Bulunduğumuz klasör yolu bulunur.

print(klasorYolu)
os.chdir("D:/xyz/Python_Başlangıç")
print(os.getcwd())
#Klasöre girir girmediğimizi kontrol ediyoruz.

os.chdir("D:/xyz/Python_Başlangıç")
klasorIcerigi = os.listdir()
#Klasör içeriğini bulur.

"""
for dosya in klasorIcerigi:
    if dosya.endswith(".py"):
    #dosyanın sonunda '.py' olanları bulur.
        print(dosya)
"""
        
klasorIcerigi2 = os.listdir("D:/xyz/Python_Başlangıç")
#Hedef klasör içeriği bulunur.

#os.mkdir("klasör2")
#Klasör oluşturur.
#Varolan klasörlerle çalışılamaz.

#os.makedirs("klasör3/klasör4/klasör5")
#İç içe klasör oluşturulur.

#os.rmdir("klasör2")
#Silinmek istenen klasörün içi boş olmalıdır. İçinde dosya olan klasör silinemez.

dosyaBilgileri = os.stat("Bahadırla Oyunumuz.py")
#print(dosyaBilgileri)
#İstenen dosyanın bilgileri ekrana yazdırılır.

for klasor in klasorIcerigi:
    if klasor.endswith(".py"):
        print("\n Dosya Adı: {} \n Dosya Bilgileri: {}".format(klasor,os.stat(klasor)))