# range 和 slice有点类似

print(range(10)) # range(0, 10)

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 3))) # [1, 4, 7]


# 第三个参数使用负数
print(list(range(8, -16, -3))) # [8, 5, 2, -1, -4, -7, -10, -13]
print(list(range(8, 16, -3))) # [] 注意 start和stop的顺序要和step表示的顺序一致
