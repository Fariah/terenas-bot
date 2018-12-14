import pymysql
from settings import db_user, db_password, db_name

class Database:
    def __init__(self):
        host = "localhost"
        user = db_user
        password = db_password
        db = db_name

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_jokes(self):
        self.cur.execute("SELECT text_value FROM jokes")
        result = self.cur.fetchall()

        return result