import mysql.connector

# Class for DB
class Database:
    my_db = my_cursor = None

    def __init__(self):
        global my_db, my_cursor
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        my_cursor = my_db.cursor()
        mycursor.execute("CREATE DATABASE hospital") # Creates the db

    def __del__(self):
        #     my_db.commit() initial
        my_db.commit()
      