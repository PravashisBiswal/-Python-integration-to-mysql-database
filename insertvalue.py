import mysql.connector
conn =mysql.connector.connect(host ='localhost',user='root',password='root_db',database='pythondb')
mycursor =conn.cursor()

sql ='insert into student(name,branch,id)values(%s,%s,%s)'
# val=('jhon','cse','id')
#if the user create mul  value then we can create a list
val =[('jhon','cse','56'),('mike','IT','78'),('tyson','Me','88')]
#mycursor.execute(sql,val)
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')
