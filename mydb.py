import mysql.connector
database =mysql.connector.connect(
    host="localhost",
    user='root',
    password='ademesscv73'
)

cursor=database.cursor()

cursor.execute("CREATE DATABASE mydatabase;")
print('ALL Done')