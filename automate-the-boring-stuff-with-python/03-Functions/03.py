def test(divide_by):
    try:
        return 100 / divide_by
    except ZeroDivisionError:
        print('不正确的参数')

print(test(1))
print(test(2))
print(test(3))
print(test(0))


# def test_1():
#     num = int(input('请输入一个数字：'))
#     while num != 1:
#         if num % 2 == 1:
#             num = num * 3 + 1
#         else:
#             num = num // 2
#         print(num)
#
# test_1()