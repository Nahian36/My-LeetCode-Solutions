def singleNumber(nums: list[int]):
    return [i for i in nums if nums.count(i) == 1][0]
    

print(singleNumber(nums = [2,2,1]))
print(singleNumber(nums = [4,1,2,1,2]))
print(singleNumber(nums = [1]))