f = open('./test.md', 'r')
print(f.read())
f.close()

try:
    f1 = open('./test.md', 'r')
    print(f1.read())
finally:
    if f1:
        f1.close()

with open('./test.md', 'r') as f:
    print(f.read())


with open('./test.md', 'r') as f:
    print(f.readline())
    # 紧接着前面的读取
    print(f.readlines())

with open('./test.md', 'r') as f:
    for line in f.readlines():
        print(line)

with open('./js.png', 'rb') as f:
    print(f.read())

with open('./test', 'a') as f:
    f.write('Hello, World!')

with open('./test1', 'a') as f:
    f.write('Hello, World!')