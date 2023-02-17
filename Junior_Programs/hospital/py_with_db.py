# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE hospital")

# THE ABOVE CODE CREATED THE DB

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for exist in mycursor:
#     print(exist)

# THE ABOVE CODE CONFIRMS THAT THE DB IS ACTUALLY THERE

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="hospital"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE daktari (FIRST_NAME VARCHAR(255), LAST_NAME VARCHAR(255), AGE INT(3), GENDER VARCHAR(8), SPECIALITY VARCHAR(255), INCOME decimal(15,2))")

# THE ABOVE CODE CREATES THE TABLE

# INSERTING THE DATA
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='', host='localhost', database='hospital')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO daktari(FIRST_NAME, LAST_NAME, AGE, GENDER, SPECIALITY,INCOME)VALUES('Coronasias', 'Onyango', 40, 'MLAE', 80000)"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()



























# import mysql.connector

# # Class for DB
# class Database:
#     my_db = my_cursor = None

#     def __init__(self):
#         global my_db, my_cursor
#         my_db = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="hospital"
#         )
#         my_cursor = my_db.cursor()
#         mycursor.execute("CREATE DATABASE hospital") # Creates the db
#         # Check if db exists
#         mycursor.execute("SHOW DATABASES")

#         for exist in mycursor:
#             print(exist)
#         # Fill in data to the db "hospital"
#         mycursor.execute("CREATE TABLE doctor (name VARCHAR(255), speciality VARCHAR(255))")

#     def __del__(self):
#         #     my_db.commit() initial
#         my_db.commit()
      