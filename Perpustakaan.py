import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from EntryForm import *
from InputForm import *
class MainForm(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()
    
    def setupUi(self):
        self.resize(600, 700)
        self.move(400, 0)
        self.setWindowTitle('DATA BUKU')
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #86A8E7, stop:1 #91EAE4);")

        self.logo = QLabel()
        self.labelJudul = QLabel()
        self.logo.setText('<img src = "bg1.jpg">')
        self.logo.setAlignment(Qt.AlignCenter)


        self.labelJudul.setText('<b><font size = 8 > DATA BUKU</font></b>')
        self.labelJudul.setStyleSheet('font-family: Product sans;')
        self.labelJudul.setAlignment(Qt.AlignCenter)

        self.table = QTableWidget()
        
        self.addButton = QPushButton()
        self.addButton.setText('Tambah Data')
        self.addButton.setStyleSheet('background-color:rgb(51,51,255);color : white');
        
        self.editButton = QPushButton()
        self.editButton.setText('Edit Data')
        self.editButton.setStyleSheet('background-color:rgb(51,51,255);color : white');

        self.deleteButton = QPushButton()
        self.deleteButton.setText('Hapus Data')
        self.deleteButton.setStyleSheet('background-color:rgb(255,0,0);color : white');

        self.exitButton = QPushButton()
        self.exitButton.setText('Keluar')
        self.exitButton.setStyleSheet('background-color:rgb(255,0,0);color : white');
        

        hbox = QHBoxLayout()
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.editButton)
        hbox.addWidget(self.deleteButton)
        hbox.addWidget(self.exitButton)
        hbox.addStretch()
        

        layout = QVBoxLayout()
        layout.addWidget(self.labelJudul)
        layout.addWidget(self.logo)
        layout.addWidget(self.table)
        layout.addLayout(hbox)
        self.setLayout(layout)
        self.addButton.clicked.connect(self.addButtonClick)
        self.editButton.clicked.connect(self.editButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.exitButton.clicked.connect(self.ExitClick)
    
    def loadData(self):
        self.table.clear()
        self.table.setRowCount(self.getRowCount())
        self.table.setColumnCount(4)
        columnHeaders = ['ID_Buku', 'Judul_Buku', 'Pengarang', 'Penerbit']
        self.table.setHorizontalHeaderLabels(columnHeaders)
        query = QSqlQuery()
        ID_BUKU, JUDUL_BUKU, PENGARANG, PENERBIT = range(4)
        row = 0
        query.exec_('SELECT * FROM DataBuku')
        while query.next():
            for i in range(5):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.table.setItem(row, i, item)
            row += 1
        item = QTableWidgetItem()
        item.setText(str(self.getRowCount()))
        self.table.setItem(6, 0, item)
    
    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM DataBuku')
        query.next()
        rowCount = query.value(0)
        return rowCount
    
    def addButtonClick(self):
        self.InputForm = InputForm()
        self.InputForm.setWindowTitle('Tambah Data Buku')
        self.mode = 0
        if self.InputForm.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
        query = QSqlQuery()
        query.exec_("INSERT INTO DataBuku VALUES (%d, '%s', '%s','%s')" %
        (id,
        self.InputForm.judulEdit.text(),
        self.InputForm.pengarangEdit.text(),
        self.InputForm.penerbitEdit.text()))
        self.loadData()
    
    def editButtonClick(self):
        self.entryForm = EntryForm()
        self.entryForm.setWindowTitle('Edit Data Buku')
        self.mode = 1
        self.entryForm.judulEdit.setText(
            self.table.item(self.table.currentRow(), 1).text())
        self.entryForm.pengarangEdit.setText(self.table.item(
            self.table.currentRow(), 2).text())
        self.entryForm.penerbitEdit.setText(self.table.item(
            self.table.currentRow(), 3).text())
        if self.entryForm.exec_() == QDialog.Accepted:
            id = int(self.table.item(self.table.currentRow(),0).text())
            query = QSqlQuery()
            query.exec_('''UPDATE DataBuku SET Judul_Buku = '%s', Pengarang = '%s', Penerbit ='%s' WHERE ID_Buku = %d''' %
            (self.entryForm.judulEdit.text(), self.entryForm.pengarangEdit.text(), self.entryForm.penerbitEdit.text(), id))
            self.loadData()
    
    def deleteButtonClick(self):
        id = int(self.table.item(self.table.currentRow(),0).text())
        quit_msg = "Anda yakin mau menghapus data?"
        dialog = QMessageBox.question(self, 'Peringatan Hapus Data', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if dialog == QMessageBox.Yes:
            query = QSqlQuery()
            query.exec_('DELETE FROM DataBuku WHERE ID_Buku = %d' %id)
            self.loadData()

    def ExitClick(self):
        quit_msg = "Anda yakin mau keluar?"
        dialog = QMessageBox.question(self, 'Peringatan', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if dialog == QMessageBox.Yes:
            self.close()
            

if __name__ == '__main__':
    a = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('DBPerpustakaan')
    
    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)

    form = MainForm()
    form.show()
    a.exec_()