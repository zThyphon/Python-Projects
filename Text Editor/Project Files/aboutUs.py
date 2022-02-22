import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon

title_font = QFont("Arial Black",24)
label_font = QFont("Verdana",14)


class AboutUs(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(450,150,450,450)
        self.setWindowIcon(QIcon("icons/help.png"))
        self.setWindowTitle("About Us")
        self.setFixedSize(self.size())

        self.UI()

    def UI(self):
        self.title = QLabel("About Us",self)
        self.title.setFont(title_font)
        self.title.move(150,80)

        self.label = QLabel("This Application Developed by zThyphon",self)
        self.label.setFont(label_font)
        self.label.move(20,200)


        self.show()


