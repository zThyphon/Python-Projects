import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPixmap
import qrcode

başlık_font = QFont("Arial Black",24)
buton_font = QFont("Verdana",14)
yazı_font = QFont("Century",20)

class Create(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Qr Code")
        self.setGeometry(700,250,650,550)
        self.setWindowIcon(QIcon("images\qricon.png"))
        self.setStyleSheet("background-color:#00BFFF")

        self.UI()

    def UI(self):

        başlık = QLabel("Create QR Code",self)
        başlık.setFont(başlık_font)
        icon = QPixmap("images\qricon_48px.png")
        qr_icon = QLabel(self)
        qr_icon.setPixmap(icon)

        horizontal = QHBoxLayout()
        horizontal.addStretch()
        horizontal.addWidget(qr_icon)
        horizontal.addWidget(başlık)
        horizontal.addStretch()

        horizontal2 = QHBoxLayout()
        self.entry_label = QLabel("Enter link: ")
        self.entry_label.setFont(yazı_font)
        self.entry_line = QLineEdit()
        self.entry_line.setPlaceholderText("Enter link here")



        horizontal2.addStretch()
        horizontal2.addWidget(self.entry_label)
        horizontal2.addWidget(self.entry_line)
        horizontal2.addStretch()

        horizontal3 = QHBoxLayout()

        create_buton = QPushButton("Create",self)
        create_buton.setStyleSheet("background-color:white")
        create_buton.setFont(buton_font)
        create_buton.clicked.connect(self.Create_QR_Code)


        horizontal3.addStretch()
        horizontal3.addWidget(create_buton)
        horizontal3.addStretch()

        horizontal4 = QHBoxLayout()
        self.entry_label2 = QLabel("Name of file: ")
        self.entry_label2.setFont(yazı_font)
        self.entry_line2 = QLineEdit()
        self.entry_line2.setPlaceholderText("Enter file name here")

        horizontal4.addStretch()
        horizontal4.addWidget(self.entry_label2)
        horizontal4.addWidget(self.entry_line2)
        horizontal4.addStretch()

        vertical = QVBoxLayout()
        vertical.addStretch()
        vertical.addLayout(horizontal)
        vertical.addLayout(horizontal2)
        vertical.addLayout(horizontal4)
        vertical.addLayout(horizontal3)
        vertical.addStretch()
        self.setLayout(vertical)


        self.show()

    def Create_QR_Code(self):
        try:
            data = self.entry_line.text()
            image = qrcode.make(data)
            save_name = self.entry_line2.text()
            file_name = save_name+".png"
            image.save(file_name)
            QMessageBox.information(self, "QR Code Created", "QR Code Created Successfully")
            image.show()


        except:
            QMessageBox.information(self,"Fail","QR Code Couldn't Created Please Check Your Entries")

