import mysql.connector
try:
    mydb = mysql.connector.connect(host="localhost", user="root", password = "BOOK-08072022")
except mysql.connector.Error as e:
    print("Cannot connect", e)


my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")

my_cursor.close()
mydb.close()