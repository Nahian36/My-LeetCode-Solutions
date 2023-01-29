def removeElement(nums: list[int], val: int):
    nums[:] = list(filter((val).__ne__, nums))
    return len(nums)

nums = [3,2,2,3]
print(removeElement(nums, 3))
print(nums)
nums = [0,1,2,2,3,0,4,2]
print(removeElement(nums, 2))
print(nums)