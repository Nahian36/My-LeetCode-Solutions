def removeDuplicates(nums: list[int]):
    ans, nums[:] = len(set(nums)), sorted(list(set(nums))) + ([0] * (len(nums) - len(set(nums))))
    return ans

nums = [1,1,2]
print(removeDuplicates(nums))
print(nums)
nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums))
print(nums)