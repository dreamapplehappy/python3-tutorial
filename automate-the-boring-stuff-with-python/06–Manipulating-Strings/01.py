test = 'I am dreamapple'
print(test)

test1 = "I'm dreamapple"
print(test1)

test2 = 'That is Alice\'s cat'
print(test2)

test3 = 'Hello there!\nHow are you?\nI\'m doing fine'
print(test3)

# 原始字符串
test4 = r'Hello there!\nHow are you?\nI\'m doing fine'
print(test4)

test5 = '''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob'''
print(test5)

"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

test6 = 'Hello World!'
print(test6[:])
print(test6[:5])
print(test6[:-7])
print(test6[1:3])
print(test6[1])
print(test6[3])

print('He' in test6)
print('Hero' in test6)
print('World' in test6)
print('W' in test6)