import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('INSERT INTO user (id, name) VALUES (\'2\', \'Dreamapple\')')
print(cursor.rowcount)

values = cursor.execute('SELECT * FROM user WHERE id=?', ('2'))
print(values.fetchall())

cursor.close()

conn.close()