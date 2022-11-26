#Import Libraries

#Import System Library
import sys
#Import PyQt5 (User Interface) Library
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon

#Define Fonts
title_font = QFont("Arial Black",24)
label_font = QFont("Verdana",14)

#Define Class
class AboutUs(QDialog):
    def __init__(self):
        super().__init__()
        
        #Define Window Attributes
        self.setGeometry(450,150,450,450)
        self.setWindowIcon(QIcon("icons/help.png"))
        self.setWindowTitle("About Us")
        self.setFixedSize(self.size())

        self.UI()
    
    #User Interface
    def UI(self):
        #About Us Title
        self.title = QLabel("About Us",self)
        self.title.setFont(title_font)
        self.title.move(150,80)
        
        #About Us Label
        self.label = QLabel("This Application Developed by zThyphon",self)
        self.label.setFont(label_font)
        self.label.move(20,200)


        self.show()


