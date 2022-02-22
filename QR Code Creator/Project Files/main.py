import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPixmap

import aboutus
import create

başlık_font = QFont("Arial",24)
buton_font = QFont("Verdana",14)
yazı_font = QFont()
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR CODE Creator by zThyphon")
        self.setGeometry(700,250,650,550)
        self.setWindowIcon(QIcon("images\qricon.png"))
        self.setStyleSheet("background-color:#00BFFF")

        self.UI()

    def UI(self):

        ### Başlık ###
        başlık = QLabel("QR CODE Creator by zThyphon",self)
        başlık.setFont(başlık_font)
        başlık.move(70,10)
        başlık_qr_code = QLabel(self)
        başlık_qr_code.setPixmap(QPixmap("images\qricon_48px.png"))
        başlık_qr_code.move(10,10)

        ### Butonlar ###
        create_buton = QPushButton("Create a QR CODE",self)
        create_buton.resize(250,50)
        create_buton.setStyleSheet("background-color:white")
        create_buton.setFont(buton_font)
        create_buton.setIcon(QIcon("images\create.png"))
        create_buton.clicked.connect(self.Create_QR)

        about_us_buton = QPushButton("About Us",self)
        about_us_buton.resize(250,50)
        about_us_buton.setStyleSheet("background-color:white")
        about_us_buton.setFont(buton_font)
        about_us_buton.move(200,220)
        about_us_buton.setIcon(QIcon("images\info.png"))
        about_us_buton.clicked.connect(self.About_us)

        exit_buton = QPushButton("Exit",self)
        exit_buton.resize(250,50)
        exit_buton.setStyleSheet("background-color:white")
        exit_buton.setFont(buton_font)
        exit_buton.move(200,310)
        exit_buton.setIcon(QIcon("images\exit.png"))
        exit_buton.clicked.connect(self.Exit_application)

        horizontal = QHBoxLayout()
        horizontal.addStretch()
        horizontal.addWidget(başlık_qr_code)
        horizontal.addWidget(başlık)
        horizontal.addStretch()

        vertical = QVBoxLayout()
        vertical.addStretch()
        vertical.addLayout(horizontal)
        vertical.addWidget(create_buton)
        vertical.addWidget(about_us_buton)
        vertical.addWidget(exit_buton)
        vertical.addStretch()

        horizontal2 = QHBoxLayout()
        horizontal2.addStretch()
        horizontal2.addLayout(vertical)
        horizontal2.addStretch()

        self.setLayout(horizontal2)
        self.setLayout(vertical)

        self.show()


    def Exit_application(self):
        onay = QMessageBox.question(self,"Exit","Do You Want to Exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if onay == QMessageBox.Yes:
            sys.exit()

    def About_us(self):
        self.about_us_shower = aboutus.About_Us()
        self.about_us_shower.show()

    def Create_QR(self):
        self.Creator = create.Create()
        self.Creator.show()



uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())