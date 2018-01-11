class Student(object):
    def __init__(self, name):
        self.name = name

    # 使用__str__
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        else:
            raise AttributeError('\'Student\' has no attribute \'%s\'' % attr)

    def __call__(self):
        print('My name is %s' % self.name)


s = Student('dreamapple')
s()
print(s)
print(s.age())
# print(s.something) # 这里会出错


class Fibonacci(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


fib = Fibonacci()

for n in fib:
    print(n)
print('------ divider ------')
print(fib[0])
print(fib[1])
print(fib[2])
print(fib[3])
print(fib[4])
print(fib[0:5])
print(fib[:10])
print('------ divider ------')


class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__


print(Chain().user.run)  # /user/run
print(Chain().asd)

print('------ divider ------')

print(callable(Student('dream')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
