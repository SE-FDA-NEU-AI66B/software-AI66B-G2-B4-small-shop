import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="mini_shop"
)

print("MySQL connection successful!")

connection.close()