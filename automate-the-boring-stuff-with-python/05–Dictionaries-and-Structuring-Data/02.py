import pprint

def charactercount(words):
    count = {}
    for c in words:
        count.setdefault(c, 0)
        count[c] = count[c] + 1
    # pprint.pprint(count)
    print(pprint.pformat(count))
charactercount('Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. A consequence is that, in general, the decimal floating-point numbers you enter are only approximated by the binary floating-point numbers actually stored in the machine.')


