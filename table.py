from PyQt5.QtSql import *
def connect():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('DBPerpustakaan')
    if db.open():
        print('Koneksi Berhasil')
        query = QSqlQuery()
        sql='''Create TABLE DataBuku(ID_Buku integer, Judul_Buku varchar(25), Pengarang varchar(15), Penerbit varchar(15))'''
    query.exec_(sql)
    if(query.exec_):
        print('Berhasil membuat Tabel')
    else:
        print('ERROR: ' + db.lastError().text())
connect()