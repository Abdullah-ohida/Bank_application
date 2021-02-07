# First import mysql connect
import mysql.connector as mysql

# Import the error module from mysql connector
from mysql.connector import Error

# connect to data base
"""create connection to database"""
connection = mysql.connect(
    host = "localhost",
    user = "Whalewalker",
    password = "#Wisdom!123",
    auth_plugin = "mysql_native_password"
)

print(connection)

cursor = connection.cursor()

# Create a database in mysql
cursor.execute("CREATE DATABASE Banking")

# show all available database in mysql
cursor.execute("SHOW DATABASES")

# fetchall data from mysql database in form of row
databases = cursor.fetchall()

print(databases)

# print out all exeiting database
for database in databases:
    print(database)

