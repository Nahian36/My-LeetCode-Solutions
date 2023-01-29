# [-1,0,1,2,-1,-4]
def threeSum(nums: list[int]):
    dct, ans, greater, smaller, zeros = {}, [], [], [], []
    for i in range(len(nums)):
        dct[nums[i]] = i
        if nums[i] > 0: greater.append(nums[i])
        elif nums[i] < 0: smaller.append(nums[i])
        else: zeros.append(nums[i])

    for i in range(len(greater)):
        for j in range(i + 1, len(greater)):
            if dct.get(0 - greater[i] - greater[j]) != None:
                new = sorted([greater[i], greater[j], 0 - greater[i] - greater[j]])
                if new not in ans: ans.append(new)

    for i in range(len(smaller)):
        for j in range(i + 1, len(smaller)):
            if dct.get(0 - smaller[i] - smaller[j]) != None:
                new = sorted([smaller[i], smaller[j], 0 - smaller[i] - smaller[j]])
                if new not in ans: ans.append(new)

    greater, smaller = list(set(greater)), list(set(smaller))
    if len(zeros) > 2: ans.append([0] * 3)

    if len(zeros):
        for i in range(len(greater)):
            if dct.get(0 - greater[i]) != None: ans.append([greater[i], 0, 0 - greater[i]])

    return ans

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))