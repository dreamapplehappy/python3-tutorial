count = 0


def test():
    print(count)


test()


def test_1():
    count = 100
    print(count)


test_1()


def test_2():
    global count
    print(count)
    count = 2


test_2()

print(count)
