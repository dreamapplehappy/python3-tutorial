
# use lambda create a anonymous function
anonymous = lambda x: x * x
print(anonymous)

l = list(map(lambda x: x + 2, [1, 2, 3, 4]))
print(l)

# generator
def generator_square_number(max):
    index = 1
    while(index < max):
        index += 1
        yield lambda index=index: index * index

gsn = generator_square_number(10)

print(next(gsn)())
print(next(gsn)())
print(next(gsn)())
