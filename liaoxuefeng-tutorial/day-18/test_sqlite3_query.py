import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('INSERT INTO user (id, name) VALUES (offical-tutorialical-tutorial\', \'Dreamapple\')')
print(cursor.rowcount)

values = cursor.execute('SELECT * FROM user WHERE id=?', ('official-tutorial'))
print(values.fetchall())

cursor.close()

conn.close()