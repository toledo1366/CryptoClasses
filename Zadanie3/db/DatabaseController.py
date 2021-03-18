import logging
import sqlite3
from sqlite3 import Error


class DbController:
    """Class which contains methods responsible for database management"""

    def createConnection(self, dbFile):
        conn = None
        try:
            conn = sqlite3.connect(dbFile)
            return conn
        except Error as e:
            logging.debug(e)
        return conn

    def createTable(self, connection):
        try:
            c = connection.cursor()
            c.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
            if c.fetchone()[0] == 0:
                c.execute("""CREATE TABLE passwords (name text NOT NULL, password text, salt text);""")
                logging.info("Given table has been created.")
            else:
                logging.info("Given table already exists.")
        except Error as e:
            logging.error(e)

    def insertData(self, data, connection):
        try:
            c = connection.cursor()
            c.execute('''INSERT INTO passwords(name, password, salt) VALUES (?, ?, ?)''', (data.name, data.password, data.salt))
            logging.info("Your account has been added to the database.")
            connection.commit()
            return c.lastrowid
        except Error as e:
            logging.error(e)

    def selectAllData(self, connection):
        c = connection.cursor()
        c.execute("SELECT * FROM passwords")
        rows = c.fetchall()
        for row in rows:
            logging.info(row)

