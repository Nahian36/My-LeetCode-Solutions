def longestCommonPrefix(strs: list[str]):
    sort, count = sorted(strs), 0
    for i in range(len(sort[0])):
        if sort[0][i] == sort[-1][i]: count += 1
        else: break
    return sort[0][:count]
    
    
print(longestCommonPrefix(["flower","flow","flower"]))