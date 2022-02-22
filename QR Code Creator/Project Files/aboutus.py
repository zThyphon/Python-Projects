import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPixmap

başlık_font = QFont("Arial Black",24)
buton_font = QFont("Verdana",14)
yazı_font = QFont("Century",20)

class About_Us(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Us")
        self.setGeometry(700,250,650,550)
        self.setWindowIcon(QIcon("images\info.png"))
        self.setStyleSheet("background-color:#00BFFF")

        self.UI()

    def UI(self):
        self.başlık = QLabel("      About Us",self)
        self.başlık.setFont(başlık_font)
        self.information = QLabel("This QR Code Creator\nDeveloped by zThyphon",self)
        self.information.setFont(yazı_font)
        self.information.move(10,10)

        vertical = QVBoxLayout()
        vertical.addStretch()
        vertical.addWidget(self.başlık)
        vertical.addStretch()
        vertical.addWidget(self.information)
        vertical.addStretch()
        vertical.addStretch()

        horizontal = QHBoxLayout()
        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addStretch()
        self.setLayout(horizontal)

        self.show()

