def hello():
    print('Hello, World!')

hello()

def test_argument(name):
    print('Hello, ' + name)

test_argument('Dreamapple')
print(test_argument('Tom')) # None

def test_1(name):
    print('Hello, ' + name)
    return name

test_1('Dreamapple')
print(test_1('Dreamapple'))

print('------')

print('my', 'name', sep='&', end='\n')
print('my', 'name', sep='&', end='.\n')

def test_2(name, age=20):
    print(name, age)
test_2('Dreamapple', 24)

