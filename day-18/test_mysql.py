import mysql.connector

conn = mysql.connector.connect(user='root', password='zxcvbnm123?', database='test')

cursor = conn.cursor()

cursor.execute('create table user (id VARCHAR(20) PRIMARY KEY , name VARCHAR(20) )')

cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

print(cursor.rowcount)

conn.commit()
cursor.close()
conn.close()