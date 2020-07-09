from PyQt5.QtSql import *
def connect():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('DBPhonebook')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()
        ID, NAMA, NOHP = range(3)
        query.exec_ ('SELECT*FROM telp_book')
        print('Output data\t: ')
        print('No.\tNama\tNo.HP')
        while query.next():
            id = query.value(ID)
            nama = query.value(NAMA)
            nohp = query.value(NOHP)
            print('%d\t%s\t%s' % (id, nama, nohp))
        else:
            print('ERROR: ' + db.lastError().text())
connect()