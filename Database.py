import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",user="root",password="",database="sql_practice")
            self.mycursor = self.conn.cursor()
        except:
            print("Connection Error")
            sys.exit(0)
        else:
            print("Connected to Database")

    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `user_info` (ID, Name, Email, Password) VALUES (NULL, '{}', '{}', '{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self,email,password):
        self.mycursor.execute("""
        SELECT * FROM `user_info` WHERE Email LIKE '{}' AND Password LIKE '{}'
        """.format(email,password))

        data=self.mycursor.fetchall()
        return data