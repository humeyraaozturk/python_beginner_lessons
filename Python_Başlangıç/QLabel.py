from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    
    app = QApplication(sys.argv)
     
    pencere = QWidget()
    
    x = QLabel(pencere)
    x.setText("Pencereye Yazı Yazabiliriz.")
    x.move(10,20)
    #Kordinatları belirliyoruz.
    
    y = QLabel(pencere)
    y.setFont(QFont("Helvetica",24,QFont.Bold))
                    #("Yazı Tipi",Boyut,Kalınlık)
    y.setText("Hello World")
    y.move(20, 40)
    
    z = QLabel(pencere)
    z.setText("<a href=www.google.com>Google</a>")   
    z.setOpenExternalLinks(True)
    z.move(40, 80)
    
    a = QLabel(pencere)
    a.setPixmap(QPixmap("C:/Users/Casper/PC Arkaplan/A village in Lofoten, Norway [2048 x 1365].jfif"))
    a.move(80, 160)
    #a.setGeometry(10,10,10,10)

    pencere.setGeometry(1000, 480, 1000, 480) 
    pencere.setWindowTitle("Yer_Tutucular")
    
    pencere.show()  
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()
    
    
    
    
    
    
    