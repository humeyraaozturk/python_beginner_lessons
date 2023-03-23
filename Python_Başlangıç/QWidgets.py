from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QWidgets")
    window.setWindowIcon(QIcon("D:\\xyz\\icon.png"))
    window.setGeometry(640, 480, 640, 480)
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    window()
    
    
    