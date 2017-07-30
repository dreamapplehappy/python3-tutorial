# slice(start, stop, step)

s_obj = slice(1, 3)

nums = [1, 2, 3, 4, 5, 6]

print(nums[s_obj]) # [2, 3]

str = 'Hello,World'

print(str[s_obj]) # el

s_obj_1 = slice(-5, None, -2)
print(str[s_obj_1]) # WolH

s_obj_2 = slice(-5, -1, -2)
print(type(str[s_obj_2])) # <class 'str'>
print(str[s_obj_2] == '') # True