import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456'
)


#prepare a cursor object using cursor() method

cursorObject = dataBase.cursor()

#creare database

cursorObject.execute("CREATE DATABASE dcrm")

print("Database created successfully")
