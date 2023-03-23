from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    
    label = QLabel("Phone Number:")
    line = QLineEdit()
    line.setInputMask("+999_999_99_99")
    
    line0 = QLineEdit("Unchangeable Text")
    line0.setReadOnly(True)
    
    label1 = QLabel("User Name:")
    line1 = QLineEdit()
    
    label2 = QLabel("Password:")
    line2 = QLineEdit()
    line2.setEchoMode(QLineEdit.Password)
    
    label3 = QLabel("Address:")
    line3 = QTextEdit()
    
    h_box = QHBoxLayout()
    h_box.addWidget(label1)
    h_box.addWidget(line1)
    
    h_box1 = QHBoxLayout()
    h_box1.addWidget(label)
    h_box1.addWidget(line)
    
    h_box2 = QHBoxLayout()
    h_box2.addWidget(label2)
    h_box2.addWidget(line2)
    
    h_box3 = QHBoxLayout()
    h_box3.addWidget(label3)
    h_box3.addWidget(line3)
    
    v_box = QVBoxLayout()
    v_box.addWidget(line0)
    v_box.addLayout(h_box)
    v_box.addLayout(h_box1)
    v_box.addLayout(h_box2)
    v_box.addLayout(h_box3)
    
    
    window.setLayout(v_box)
    window.setGeometry(640, 480, 640, 480)
    window.setWindowTitle("Inputs")
    window.show()
    sys.exit(app.exec())
    

    
if __name__ == "__main__":
    window()
    
    
    
    
    
    
    
    
    
    