import mysql.connector

database = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= ""
)

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE IF NOT EXISTS dcrm")

print("Database created successfully")