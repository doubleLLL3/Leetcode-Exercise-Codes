# nums = [4,1,2,1,2]
# for i in range(len(nums)):
#     check = nums.pop(0)
#     if check in nums:
#         nums.pop(nums.index(check))
#         print(check)
#         continue
#     print(check)
from collections import defaultdict
nums = [4,1,2,1,2]
hash_table = defaultdict(int)
for i in nums:
    hash_table[i] += 1

for i in hash_table:
    if hash_table[i] == 1:
        print(i)

    
