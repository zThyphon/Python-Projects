import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp,QSize
import time
import aboutUs

textChanged = False
url = ""
tbchecked = True
dockChecked = True
statusbarChecked = True

class FindDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Find and Replace")
        self.setWindowIcon(QIcon("icons/find.png"))
        self.setGeometry(450,250,350,200)

        self.UI()
    def UI(self):
        formLayout = QFormLayout(self)
        hbox = QHBoxLayout()
        txt_find = QLabel("Find: ")
        txt_replace = QLabel("Replace")
        txt_label = QLabel("")
        self.find_entry = QLineEdit()
        self.find_entry.setPlaceholderText("What Do You Search?")
        self.replace_entry = QLineEdit()

        self.find_button = QPushButton("Find")
        self.replace_button = QPushButton("Replace")
        self.replace_entry.setPlaceholderText("What Do You Replace?")

        hbox.addWidget(self.find_button)
        hbox.addWidget(self.replace_button)

        formLayout.addRow(txt_find,self.find_entry)
        formLayout.addRow(txt_replace,self.replace_entry)
        formLayout.addRow(txt_label,hbox)

        self.setLayout(formLayout)

        self.show()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor by zThyphon")
        self.setWindowIcon(QIcon("icons/notepad.png"))
        self.setGeometry(450,150,1000,800)

        self.UI()

    def UI(self):
        ### Text Editör ###
        self.editor = QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(12.0)
        self.editor.textChanged.connect(self.funcTextChanged)

        ### Text Editör Ana Fonksiyonlar ###
        self.menu()
        self.toolbar()
        self.dockbar()
        self.statusbar()
        self.show()

    def statusbar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def funcTextChanged(self):
        global textChanged
        textChanged = True
        text = self.editor.toPlainText()
        letters = len(text)
        words = len(text.split())
        self.status_bar .showMessage("Letters: "+str(letters)+" Words: "+str(words))


    def toolbar(self):
        ### ToolBar ###
        self.tb = self.addToolBar("ToolBar")

        ### ToolBar Font ComboBox ###
        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.changeFont)
        self.tb.addWidget(self.fontFamily)
        self.tb.addSeparator()
        self.tb.addSeparator()

        ### Toolbar FontSize ComboBox ###
        self.fontSize = QComboBox(self)
        self.tb.addWidget(self.fontSize)
        for i in range(8,101,2):
            self.fontSize.addItem(str(i))
        self.fontSize.setEditable(True)
        self.fontSize.setCurrentText("12")
        self.fontSize.currentTextChanged.connect(self.changeSize)
        self.tb.addSeparator()
        self.tb.addSeparator()

        ### ToolBar Bold Buton ###
        self.bold = QAction(QIcon("icons/bold.png"),"Bold",self)
        self.tb.addAction(self.bold)
        self.bold.triggered.connect(self.Bold)

        ### ToolBar İtalic Buton ###
        self.italic = QAction(QIcon("icons/italic.png"),"İtalic",self)
        self.tb.addAction(self.italic)
        self.italic.triggered.connect(self.Italic)

        ### ToolBar Underline Buton ###
        self.underline = QAction(QIcon("icons/underline.png"),"Underline",self)
        self.tb.addAction(self.underline)
        self.underline.triggered.connect(self.Underline)
        self.tb.addSeparator()
        self.tb.addSeparator()

        ### ToolBar Font Rengi Buton ###
        self.fontColor = QAction(QIcon("icons/color.png"),"Change Color",self)
        self.tb.addAction(self.fontColor)
        self.fontColor.triggered.connect(self.funcFontColor)

        ### ToolBar Font Arkaplan Rengi Buton ###
        self.fontBackColor = QAction(QIcon("icons/backcolor.png"),"Change Background Color",self)
        self.tb.addAction(self.fontBackColor)
        self.fontBackColor.triggered.connect(self.funcBackColor)
        self.tb.addSeparator()
        self.tb.addSeparator()

        ### ToolBar Sola Hizalama Buton ###
        self.alignLeft = QAction(QIcon("icons/alignleft.png"),"Align Left",self)
        self.tb.addAction(self.alignLeft)
        self.alignLeft.triggered.connect(self.funcAlignLeft)

        ### ToolBar Ortaya Hizalama Buton ###
        self.alignCenter = QAction(QIcon("icons/aligncenter.png"),"Align Center",self)
        self.tb.addAction(self.alignCenter)
        self.alignCenter.triggered.connect(self.funcAlignCenter)
        ### ToolBar Sağa Hizalama Buton ###
        self.alignRight = QAction(QIcon("icons/alignright.png"),"Align Right",self)
        self.tb.addAction(self.alignRight)
        self.alignRight.triggered.connect(self.funcAlignRight)
        ### ToolBar Justify Buton ###
        self.alignjustify = QAction(QIcon("icons/alignJustify.png"),"Align Justify",self)
        self.tb.addAction(self.alignjustify)
        self.alignjustify.triggered.connect(self.funcAlignJustify)
        self.tb.addSeparator()
        self.tb.addSeparator()

        ### ToolBar Listeleme Buton ###
        self.bulletList = QAction(QIcon("icons/bulletlist.png"),"Bullet List",self)
        self.tb.addAction(self.bulletList)
        self.bulletList.triggered.connect(self.funcBulletList)

        ### ToolBar Numara Listeleme Buton ###
        self.numberList = QAction(QIcon("icons/numberlist.png"),"Number List",self)
        self.tb.addAction(self.numberList)
        self.numberList.triggered.connect(self.funcNumberList)

    def funcBulletList(self):
        self.editor.insertHtml("<ul><li><h3>&nbsp;</h3></li></ul>")

    def funcNumberList(self):
        self.editor.insertHtml("<ol><li><h3>&nbsp;</h3></li></ol>")
    def funcAlignLeft(self):
        self.editor.setAlignment(Qt.AlignLeft)

    def funcAlignCenter(self):
        self.editor.setAlignment(Qt.AlignCenter)

    def funcAlignRight(self):
        self.editor.setAlignment(Qt.AlignRight)

    def funcAlignJustify(self):
        self.editor.setAlignment(Qt.AlignJustify)

    def funcBackColor(self):
        bcolor = QColorDialog.getColor()
        self.editor.setTextBackgroundColor(bcolor)

    def funcFontColor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)
    def Bold(self):
        fontWeight = self.editor.fontWeight()
        if fontWeight == 50:
            self.editor.setFontWeight(QFont.Bold)

        elif fontWeight == 75:
            self.editor.setFontWeight(QFont.Normal)

    def Italic(self):
        italic = self.editor.fontItalic()
        if italic == True:
            self.editor.setFontItalic(False)
        else:
            self.editor.setFontItalic(True)

    def Underline(self):
        underline = self.editor.fontUnderline()
        if underline == True:
            self.editor.setFontUnderline(False)

        else:
            self.editor.setFontUnderline(True)

    def changeFont(self,font):
        font = QFont(self.fontFamily.currentFont())
        self.editor.setCurrentFont(font)

    def changeSize(self,size):
        self.editor.setFontPointSize(float(size))
        ### ToolBar Bitiş ###


    def dockbar(self):
        self.dock = QDockWidget("Short Cuts",self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock)
        self.dockWidget = QWidget(self)
        self.dock.setWidget(self.dockWidget)
        formlayout = QFormLayout()

        ### DockBar Butonları ###

        ### Bul Buton ###
        btn_Find = QToolButton()
        btn_Find.setIcon(QIcon("icons/find_large.png"))
        btn_Find.setText("Find")
        btn_Find.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn_Find.setIconSize(QSize(50,50))
        btn_Find.setCheckable(True)
        btn_Find.toggled.connect(self.Find)


        ### Yeni Buton ###
        btn_New = QToolButton()
        btn_New.setIcon(QIcon("icons/new_large.png"))
        btn_New.setText("New File")
        btn_New.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn_New.setIconSize(QSize(50,50))
        btn_New.setCheckable(True)
        btn_New.toggled.connect(self.newFile)

        ### Aç Buton ###
        btn_Open = QToolButton()
        btn_Open.setIcon(QIcon("icons/open_large.png"))
        btn_Open.setText("Open File")
        btn_Open.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn_Open.setIconSize(QSize(50,50))
        btn_Open.setCheckable(True)
        btn_Open.toggled.connect(self.openFile)

        ### Kaydet Buton ###
        btn_Save = QToolButton()
        btn_Save.setIcon(QIcon("icons/save_large.png"))
        btn_Save.setText("Save")
        btn_Save.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn_Save.setIconSize(QSize(50,50))
        btn_Save.setCheckable(True)
        btn_Save.toggled.connect(self.saveFile)

        ### Butonları Form Layouta Ekleme ###
        formlayout.addRow(btn_Find,btn_New)
        formlayout.addRow(btn_Open,btn_Save)
        self.dockWidget.setLayout(formlayout)

    def menu(self):
        ### Ana Menüler ###
        self.menubar = self.menuBar()
        self.menubar.resize(160,20)
        file = self.menubar.addMenu("File")
        edit = self.menubar.addMenu("Edit")
        view = self.menubar.addMenu("View")
        help_menu = self.menubar.addMenu("Help")

        ### Alt Menüler ###


        ### FİLE ARA MENÜLERİ ###

        ### New Ara Menüsü ###
        new = QAction(QIcon("icons/new.png"),"New",self)
        new.setShortcut("Alt+Insert")
        new.triggered.connect(self.newFile)
        file.addAction(new)
        ### Open Ara Menüsü ###
        open = QAction(QIcon("icons/open.png"),"Open File",self)
        open.setShortcut("Ctrl+O")
        file.addAction(open)
        open.triggered.connect(self.openFile)
        ### Save Ara Menüsü ###
        save = QAction(QIcon("icons/save.png"),"Save",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        save.triggered.connect(self.saveFile)
        ### Exit Ara Menüsü ###
        exit_ = QAction(QIcon("icons/exit.png"),"Exit",self)
        file.addAction(exit_)
        exit_.triggered.connect(self.exitFile)

        ### EDİT ARA MENÜLERİ ###

        ### Undo Ara Menü ###
        undo = QAction(QIcon("icons/undo.png"),"Undo",self)
        undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.Undo)
        edit.addAction(undo)

        ### Cut Ara Menüsü ###
        cut = QAction(QIcon("icons/cut.png"),"Cut",self)
        cut.setShortcut("Ctrl+X")
        cut.triggered.connect(self.Cut)
        edit.addAction(cut)

        ### Copy Ara Menüsü ###
        copy = QAction(QIcon("icons/copy.png"),"Copy",self)
        copy.setShortcut("Ctrl+C")
        copy.triggered.connect(self.Copy)
        edit.addAction(copy)

        ### Paste Ara Menüsü ###
        paste = QAction(QIcon("icons/paste.png"),"Paste",self)
        paste.setShortcut("Ctrl+V")
        paste.triggered.connect(self.Paste)
        edit.addAction(paste)

        ### Find Ara Menüsü ###
        find = QAction(QIcon("icons/find.png"),"Find",self)
        find.setShortcut("Ctrl+F")
        find.triggered.connect(self.Find)
        edit.addAction(find)

        ### Time and Date Ara Menüsü ###
        time_date = QAction(QIcon("icons/datetime.png"),"Insert Time and Date",self)
        time_date.setShortcut("Ctrl+5")
        time_date.triggered.connect(self.Time_Date)
        edit.addAction(time_date)

        ### VİEW ARA MENÜLERİ ###

        ### Toggle StatusBar Ara Menüsü ###
        toggle_Statusbar = QAction("Toggle StatusBar",self,checkable=True)
        toggle_Statusbar.triggered.connect(self.funcToggleStatusBar)
        view.addAction(toggle_Statusbar)

        ### Toggle ToolBar Ara Menüsü ###
        toggle_Toolbar = QAction("Toggle Toolbar",self,checkable=True)
        toggle_Toolbar.triggered.connect(self.funcToggleToolBar)
        view.addAction(toggle_Toolbar)

        ### Toggle DockBar ###
        toggle_DockBar = QAction("Toggle Dockbar",self,checkable=True)
        toggle_DockBar.triggered.connect(self.funcToggleDockBar)
        view.addAction(toggle_DockBar)

        ### Help Ara Menüleri ###
        about_us = QAction(QIcon("icons/help.png"),"About Us",self)
        about_us.triggered.connect(self.About)
        help_menu.addAction(about_us)




    ### Menü Fonksiyonları ###
    def newFile(self):
        try:
            global url
            url = ""
            self.editor.clear()

        except:
            pass

    def openFile(self):
        global url
        try:
            url = QFileDialog.getOpenFileName(self,"Open File","","All Files(*);;Txt Files *txt")
            with open(url[0],"r+",encoding="utf-8") as file:
                content = file.read()
                self.editor.clear()
                self.editor.setText(content)


        except:
            pass


    def saveFile(self):
        global url
        try:
            if textChanged == True:
                if url != "":
                    content = self.editor.toPlainText()
                    with open(url[0],"w",encoding="utf_8") as file:
                        file.write(content)
                    QMessageBox.information(self, "Save Information", "Changes Saved")
                else:
                    url = QFileDialog.getSaveFileName(self,"Save File","","Txt Files (*.txt")
                    content2 = self.editor.toPlainText()
                    with open(url[0],"w",encoding="utf-8") as file2:
                        file2.write(content2)


        except:
            pass

    def exitFile(self):
        global url
        try:
            if textChanged == True:
                check = QMessageBox.information(self,"Information","Do You Want to Save This File?", QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

                if check == QMessageBox.Save:
                    if url != "":
                        content = self.editor.toPlainText()
                        with open(url[0],"w",encoding="utf-8") as file:
                            file.write(content)

                    else:
                        url = QFileDialog.getSaveFileName(self,"Save File","","Txt files(*.txt)")
                        content2 = self.editor.toPlainText()
                        with open(url[0],"w",encoding="utf-8") as file2:
                            file2.write(content2)

                elif check == QMessageBox.No:
                    qApp.quit()

            else:
                qApp.quit()
        except:
            pass

    def Undo(self):
        self.editor.undo()

    def Cut(self):
        self.editor.cut()

    def Copy(self):
        self.editor.copy()

    def Paste(self):
        self.editor.paste()

    def Find(self):
        self.find = FindDialog()
        self.find.show()

        def findWords():
            global word
            word = self.find.find_entry.text()
            if word !="":
                cursor = self.editor.textCursor()
                format = QTextCharFormat()
                format.setBackground(QBrush(QColor("yellow")))
                regex = QRegExp(word)
                pos = 0
                index = regex.indexIn(self.editor.toPlainText(),pos)
                self.count = 0
                while(index != -1):
                    cursor.setPosition(index)
                    cursor.movePosition(QTextCursor.EndOfWord,1)
                    cursor.mergeCharFormat(format)
                    pos = index + regex.matchedLength()
                    index = regex.indexIn(self.editor.toPlainText(),pos)
                    self.count +=1
                self.status_bar.showMessage(str(self.count) + " Result Found")
            else:
                QMessageBox.information(self,"Warning","You Should Entry a Word")

        def replaceWords():
            replaceText = self.find.replace_entry.text()
            word = self.find.find_entry.text()
            text = self.editor.toPlainText()
            newValue = text.replace(word,replaceText)
            self.editor.clear()
            self.editor.append(newValue)
            self.status_bar.showMessage("Operation Complated")

        self.find.find_button.clicked.connect(findWords)
        self.find.replace_button.clicked.connect(replaceWords)


    def Time_Date(self):
        time_date = time.strftime("%d.%m.%y %H:%M")
        self.editor.append("Date and Time: "+time_date)


    def funcToggleStatusBar(self):
        global statusbarChecked
        if statusbarChecked == True:
            self.status_bar.hide()
            statusbarChecked = False
        else:
            self.status_bar.show()
            statusbarChecked = True

    def funcToggleToolBar(self):
        global tbchecked
        if tbchecked == True:
            self.tb.hide()
            tbchecked = False
        else:
            self.tb.show()
            tbchecked = True

    def funcToggleDockBar(self):
        global dockChecked
        if dockChecked == True:
            self.dock.hide()
            dockChecked = False
        else:
            self.dock.show()
            dockChecked = True

    def About(self):
        self.about = aboutUs.AboutUs()
        self.about.show()
    ### Menü Fonksiyonları Bitiş ###



def main():
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()