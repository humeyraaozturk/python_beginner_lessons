import random
import time

def başlangıç():
    print("Vaktiyle çok yüksek surları olan ve bir kral tarafından yönetilen bir şehir varmış.")
    time.sleep(1)
    print("Halk huzur içinde yaşıyormuş...")
    time.sleep(2)
    
    print("Günlerden bir gün ormandan gelen iki ejderha şehrin iki giriş kapısının önüne oturmuş.")
    time.sleep(1)
    print("Önünde iki tane kapı var")
    time.sleep(1)
    print("Birini seçmeniz gerekiyor")
    time.sleep(3)
    
    print("Kapıların ardında iki tane ejderha var.")
    time.sleep(1)
    print("Ejderhalardan biri dost canlısı ve sizi kurtarmak istiyor.")
    time.sleep(1)
    print("Diğeri ise kana susamış ve herkesi öldürüyor...")
    time.sleep(2)
    
def yol_seç():
    karar = int(input("Bir yol seçmen gerek.  1 mi? / 2 mi? =>"))
 
def ilerle(x):
    print("Yola doğru ilerliyorsun..")
    time.sleep(1)
    print("Karanlık sisli bir hava var.")
    time.sleep(1)
    print("Karşında bir ejderha var.")
    time.sleep(1)
    print("Ejderha ağzını açıyor.")
    time.sleep(1)
    print("Vee...")
    time.sleep(2)
    
    if x == random.randint(1,2):
        print("Merhaba, beni takip et. Seni ve halkını kurtaracağım...")
        time.sleep(1)
        print("İyi ejderha ile karşılaştınız.")
        time.sleep(1)
        print("Oyunu kazandınız.")
        time.sleep(1)
    else:
        print("Kaçma! Ben senin sonunum!")
        time.sleep(1)
        print("Üzgünüz ama kötü ejderha tarafından öldürüldünüz.")
        time.sleep(1)
        print("Oyunu kaybettiniz.")
        time.sleep(2)
        
        
while True:
    başlangıç()
    x_name = yol_seç()
    ilerle(x_name)
    
    print("Oyuna devam etmek ister misiniz?")
    cevap = input("Evet için 1 / Hayır için 2  =>")
    if cevap == "1":
        print("Yeniden oyun başlıyor...\n")
    else:
        print("Görüşmek üzere")
        break
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    