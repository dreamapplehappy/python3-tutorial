import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE user (id varchar(20) PRIMARY KEY , name varchar(20))')

cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michael\')')

print(cursor.rowcount)

values = cursor.execute('SELECT * FROM user WHERE id=?', ('1',))
print(values.fetchall())

cursor.close()

conn.commit()
conn.close()

