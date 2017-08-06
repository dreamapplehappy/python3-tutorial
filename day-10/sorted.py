# 使用 sorted 函数

words = ['bob', 'about', 'Zoo', 'Credit']

# ['about', 'bob', 'Credit', 'Zoo']
print(sorted(words, key=str.lower))

# ['Zoo', 'Credit', 'bob', 'about']
print(sorted(words, key=str.lower, reverse=True))


# test

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L, key=by_score, reverse=True)
print(L3)

# 使用itemgetter

from operator import itemgetter

L4 = sorted(L, key=itemgetter(0))
L5 = sorted(L, key=itemgetter(1), reverse=True)
print(L4)
print(L5)