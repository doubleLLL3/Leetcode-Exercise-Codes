def moveZeroes(nums):
    i = 0
    n = 0
    while n < len(nums): # 用len(nums)不会随着nums增加而改变(如果用in nums的话)
        if nums[i] == 0:
            nums.append(nums.pop(i))
        else:
            i += 1
        n += 1 #不管怎样要计算只遍历原数组大小的次数

moveZeroes([0,1,0,3,12])