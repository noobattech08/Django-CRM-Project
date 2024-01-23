import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='root', passwd='my#SQL#123'
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE myProjectDb")

print("ALL DONE!")
