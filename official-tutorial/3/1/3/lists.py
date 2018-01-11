# 创建一个List

squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3])
print(squares[-3:])

squares_copy = squares[:]
print(squares_copy)
# https://stackoverflow.com/questions/2988017/string-comparison-in-python-is-vs
print(squares_copy == squares)
print(squares_copy is squares)

squares_plus = squares + [81, 100, 121, 144, 169]
print(squares_plus)

squares.append(81)
print(squares)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[1] = 'z'
print(letters)

letters[1:2] = []
print(letters)

letters[2:4] = ['D', 'E']
print(letters)

print(len(letters))

nest_lists = [squares, letters]
print(nest_lists)