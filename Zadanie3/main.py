import sqlite3
import os.path
from db.DatabaseController import DbController
import src.Saver as saver


def applicationStart():
    db = DbController()
    connector = db.createConnection('zad3.db')
    with connector:
        db.createTable(connector)
        db.insertData(saver.createAccount(), connector)
        db.selectAllData(connector)

if __name__ == '__main__':
    applicationStart()
