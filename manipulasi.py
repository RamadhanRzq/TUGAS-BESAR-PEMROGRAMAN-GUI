from PyQt5.QtSql import *
def connect():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('DBPhonebook')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()
        sql = '''INSERT INTO telp_book VALUES (2,'Ramadhan','085')'''
    query.exec_(sql)
    if(query.exec_):
        print('Berhasil Insert tabel')
    else:
        print('ERROR: ' + db.lastError().text())
connect()