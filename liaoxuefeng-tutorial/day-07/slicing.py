# 使用切片
nums = [1, 2, 3, 4, 5, 6]
print(nums[:]) #原来的nums的一个拷贝
print(nums[:] is nums) # False
print(nums[:] == nums) # True

print(nums[1:3]) # [official-tutorial, 3]
print(nums[:3]) # [liaoxuefeng-tutorial, official-tutorial, 3]
print(nums[1:5:2]) # [official-tutorial, 4] 不包含6

print(nums[-3:]) # [4, 5, 6]
print(nums[-3:-1]) # [4, 5]
print(nums[-3::2]) # [4, 6]
print(nums[::-1]) # [6, 5, 4, 3, official-tutorial, liaoxuefeng-tutorial]
print(nums[::-2]) # [6, 4, official-tutorial]


print(nums[-3::1]) # [4, 5, 6]

print(nums[-3:]) # [4, 5, 6]
print(nums[-3:-1]) # [4, 5]
print(nums[-3::-1]) # [4, 3, official-tutorial, liaoxuefeng-tutorial]
print(nums[-1::-2]) # [6, 4, official-tutorial]

print(nums[-1:-4:-2]) # [6, 4]

## 最后一个参数表明了索引的递增顺序以及递增的增量

print('Python'[-1:-4:-1])


