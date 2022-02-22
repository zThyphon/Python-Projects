import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap
from pytube import YouTube

header_font = QFont("Arial", 24)
label_font = QFont("Century", 20)
button_font = QFont("Verdana", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Downloader by zThyphon")
        self.setGeometry(600, 250, 850, 650)
        self.setWindowIcon(QIcon("icons/download_icon.png"))

        self.UI()

    def UI(self):
        header_label = QLabel("Video Downloader", self)
        header_label.setFont(header_font)

        header_image = QLabel(self)
        header_image.setPixmap(QPixmap("icons/header_icon.png"))

        header_hbox = QHBoxLayout()
        header_hbox.addStretch()
        header_hbox.addWidget(header_image)
        header_hbox.addWidget(header_label)
        header_hbox.addStretch()

        info_label = QLabel("Enter Video Link")
        info_label.setFont(label_font)

        self.entry_line = QLineEdit()
        self.entry_line.setPlaceholderText("Paste Link Here")

        download_button = QPushButton("Download", self)
        download_button.setFont(button_font)
        download_button.clicked.connect(self.Download_Video)

        info_hbox = QHBoxLayout()
        info_hbox.addStretch()
        info_hbox.addWidget(info_label)
        info_hbox.addStretch()

        entry_line_hbox = QHBoxLayout()
        entry_line_hbox.addStretch()
        entry_line_hbox.addWidget(self.entry_line)
        entry_line_hbox.addStretch()

        download_hbox = QHBoxLayout()
        download_hbox.addStretch()
        download_hbox.addWidget(download_button)
        download_hbox.addStretch()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(header_hbox)
        vbox.addLayout(info_hbox)
        vbox.addLayout(entry_line_hbox)
        vbox.addLayout(download_hbox)
        vbox.addStretch()

        self.setLayout(vbox)

        self.show()

    def Download_Video(self):
        try:
            if (self.entry_line.text != ""):
                link = self.entry_line.text()
                QMessageBox.information(self, "Video Downloader", "Video is downloading")
                url = YouTube(str(link))
                video = url.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
                video.download()
                QMessageBox.information(self, "Video Downloader", "Video was successfully downloaded")
            else:
                QMessageBox.information(self, "Video Downloader", "You must enter a link")

        except:
            QMessageBox.information(self, "Video Downloader", "There occured an error during the downloading")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
