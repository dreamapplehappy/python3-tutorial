import copy

num = [1, 2, 3]
print(tuple(num))
test = (1, 2, 3)
print(list(test))
test1 = (1)
test2 = (1,)
print(type(test1))
print(type(test2))

source = [1, 2, 3, 4]
target1 = copy.copy(source)
print(target1)
target1[0] = -1
print(target1)
print(source)

source[0] = [4, 5, 6]
target2 = copy.copy(source)
print(source)
print(target2)
target2[0][0] = -1
print(target2)
print(source)

target3 = copy.deepcopy(source)
target3[0][0] = -100
print(target3)
print(source)