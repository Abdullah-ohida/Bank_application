# First import mysql connect
import mysql.connector as mysql

def use_database():
    """function create connection to database"""
    connection = None
    connection = mysql.connect(
        host = "localhost",
        user = "Whalewalker",
        password = "#Wisdom!123",
        auth_plugin = "mysql_native_password",
        database = "Banking"
    )
    return connection

# use_database()