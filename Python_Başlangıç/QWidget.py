from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
#import * => Kütüphanenin hepsi anlamına gelir.

def pencere():
    
    app = QApplication(sys.argv)
    #Program sonsuz döngüye girer.
    
    pencere = QWidget()
    
    #pencere.setWindowIcon(QIcob("icon.jpg"))
    #Pencereyi önceden belirlediğimiz bir ikon ile açabiliriz.
   
    pencere.setGeometry(640, 480, 640, 480)
    #Pencerenin geometrisini belirleyebiliriz.
    
    #pencere.setLayout(katman_adı)
    
    pencere.setWindowTitle("Pencere_Başlığı")
    #Pencereye ad verebiliriz.
    
    pencere.show()
    #Pencereyi açar.
    
    sys.exit(app.exec())

if __name__ == "__main__":
    #Dosya ana klasörün içerisindeyse çalışır.
    pencere()




