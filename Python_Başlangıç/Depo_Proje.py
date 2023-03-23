from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Ana_Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self):
        pass
    
if __name__ == "_main__":
    app =QApplication(sys.argv)
    Ana_Pencere = Ana_Pencere()
    sys.exit()
    
    
    