def twoSum(nums, target):
    for i,v in enumerate(nums):
        try:
            find = nums[i+1: len(nums)].index(target - v)
        except:
            pass
        else:
            return [i,find+i+1]
    return [-1,-1]
    
print(twoSum([2,7,11,15], 9))