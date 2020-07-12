from PyQt5.QtWidgets import (QDialog, QGridLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton)
class InputForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(300, 250)
        self.move(320, 280)
        self.mode = -1 # 0: mode tambah, 1: mode ubah
        self.okButton = QPushButton()
        self.okButton.setText('OK')
        self.okButton.setStyleSheet('background-color:rgb(51,51,255);color : white');

        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        self.label2 = QLabel("Judul_Buku")
        self.judulEdit = QLineEdit()
        self.label3 = QLabel("Pengarang")
        self.pengarangEdit = QLineEdit()
        self.label4 = QLabel("Penerbit")
        self.penerbitEdit = QLineEdit()
        if self.mode == 0:
            self.judulEdit.clear()
            self.pengarangEdit.clear()
            self.penerbitEdit.clear()
        layout = QGridLayout()
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.judulEdit, 1, 1)
        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.pengarangEdit, 2, 1)
        layout.addWidget(self.label4, 3, 0)
        layout.addWidget(self.penerbitEdit, 3, 1)
        layout.addLayout(hbox, 4, 1)
        self.setLayout(layout)
        self.okButton.clicked.connect(self.accept)