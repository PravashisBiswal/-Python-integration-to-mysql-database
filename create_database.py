import mysql.connector 

conn =mysql.connector.connect(host ='localhost',user='root',password='root_db')
if conn.is_connected():
     print('connection established')

mycursor= conn.cursor()
mycursor.execute('create database  pythondb')
print(mycursor)
