from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


def window():
    app = QApplication(sys.argv)
    window = QWidget()
    
    x = QLabel(window)
    x.setText("Game of Thrones")
    x.move(10, 20)

    y = QLabel(window)
    y.setFont(QFont("Helvatica",24,QFont.Bold))
    #Yazı tipi,boyutu,kalınlık
    y.setText("Taht Savaşları")
    y.move(10, 40)
    
    z =QLabel(window)
    z.setText("<a href = www.google.com> Google </a>")
    z.setOpenExternalLinks(True)
    z.move(10, 100)
    
    a = QLabel(window)
    a.setPixmap(QPixmap("D:\\xyz\\UAV_Task\\1645823065330"))
    a.move(10, 120)
    
    
    window.setWindowTitle("QLabel")
    window.setGeometry(640, 480, 640, 480)
    window.show()
    sys.exit(app.exec())
    
    
    
if __name__ == "__main__":
    window()
    
    
    