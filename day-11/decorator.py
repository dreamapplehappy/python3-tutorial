# decorator
def compute(x):
    return x + 1

print(compute.__name__)

# decorator is a high-level function
def log(func):
    def wrapper(*args, **kw):
        print('func call', func.__name__)
        return func(*args, **kw)
    return wrapper

# decorator
@log
def sum():
    pass

sum()

def logger(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('your args', text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('test.md')
def sum1():
    pass

sum1()

# original function __name__ change
print(sum1.__name__)

# fix the problem

import functools

def optimization_logger(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('your args', text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@optimization_logger()
def sum2():
    pass

sum2()
print(sum2.__name__)

# test.md

def test_log(argument = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(argument)
            print('before %s called' % (func.__name__))
            func(*args, **kw)
            print('after %s called' % (func.__name__))
        return wrapper
    return decorator

@test_log()
def sum3():
    pass

@test_log('sth')
def sum4():
    pass

print('------ divider ------')
sum3()
print(sum3.__name__)
sum4()
print(sum4.__name__)

print('------ divider ------')

from functools import wraps

def logX(arg):
    if callable(arg):
        func = arg
        def wrapper(*args, **kw):
            print('before')
            func(*args, **kw)
        return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kw):
                print(arg)
                print('before')
                func(*args, **kw)
            return wrapper
        return decorator

@logX
def sum7():
    pass

@logX(123)
def sum8():
    pass

sum7()
sum8()