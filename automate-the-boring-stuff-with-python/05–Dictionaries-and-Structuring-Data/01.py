dreamapple = {
    'name': 'dreamapple',
    'age': 20,
    'gender': 'man'
}

print(dreamapple)
print(dreamapple['name'])

dreamapple1 = {
    'age': 20,
    'gender': 'man',
    'name': 'dreamapple'
}

print(dreamapple == dreamapple1)

test = {
    'name': 'test',
    1: 100,
    'age': 18
}
print(test)

print(test.keys())
print(test.values())
print(test.items())

for k in test.keys():
    print(k)
for v in test.values():
    print(v)
for k, v in test.items():
    print(k, v, sep='=')

print(1 in test)
print(1 in test.values())
print((1, 100) in test.items())
print(1 in (1, 100))

print('hello' not in test)

print(test.get('hello', -1))
print(test.get(1, -1))
print(test.get('name', -1))

test['color'] = 'blue'
print(test)

print(test.setdefault('skill', 'javascript'))
print(test.setdefault('skill', 'python'))


