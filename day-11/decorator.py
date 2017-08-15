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

@logger('test')
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


