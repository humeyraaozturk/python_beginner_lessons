from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    
    photo1 = QLabel()
    photo1.setPixmap(QPixmap("D:\\xyz\\UAV_Task\\1645823065330"))
    text1 = QLabel("Landscape of Mountain")
    
    photo2 = QLabel()
    photo2.setPixmap(QPixmap("D:\\xyz\\UAV_Task\\1645823065020"))
    text2 = QLabel("North Lights")
    
    h_box1 = QHBoxLayout()
    h_box1.addWidget(photo1)
    h_box1.addStretch()
    h_box1.addWidget(text1)
    
    h_box2 = QHBoxLayout()
    h_box2.addWidget(photo2)
    h_box2.addStretch()
    h_box2.addWidget(text2)
    
    v_box = QVBoxLayout()
    v_box.addLayout(h_box1)
    v_box.addStretch()
    v_box.addLayout(h_box2)
    
    window.setLayout(v_box)
    window.setWindowTitle("Horizontal and Vertical Box")
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    window()
    
    
    