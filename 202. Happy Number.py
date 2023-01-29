def isHappy(n: int) -> bool:
    arr = str(n)
    for i in range(7):
        ans = 0
        for i in arr: ans += int(i) ** 2 
        if ans != 1: arr = str(ans)
        else: return True
    return False

print(isHappy(n = 19))
print(isHappy(n = 2))