from io import StringIO

sio = StringIO()

sio.write('Hello')
print(sio.getvalue())

print(sio.write(' '))
sio.write('World!')
print(sio.getvalue())

s = StringIO('Hello\nHi\nGoodbye')
while True:
    line = s.readline()
    if line == '':
        break
    print(line.strip())