

nums = [1,2,3,4,5,6,7]

l = len(nums)
k = 3

print(111)
print(nums[:3])
print(nums[3:])
nums[l-k:], nums[:l-k] = nums[:l-k], nums[l-k:]
print(nums[:3])
print(nums[3:])
print(nums)


nums = [1,2,3,4,5,6,7]

print(222)
print(nums[:-4])
print(nums[-4:])
nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
print(nums[:-4])
print(nums[-4:])
print(nums)
print(nums)

# !!!单步运行这两段代码即可
nums = [1,2,3,4,5,6,7]
tmp = nums[:l-k]
nums[:l-k] = nums[l-k:]
nums[l-k:] = tmp

nums = [1,2,3,4,5,6,7]
tmp = nums[:-k]
nums[:-k] = nums[-k:]
nums[-k:] = tmp