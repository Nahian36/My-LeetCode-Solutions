def reverse(x: int):
    ans = ""
    if x < 0: ans = "-"
    ans = int(ans + str(abs(x))[::-1])
    if ans < -(2 ** 31) or ans > (2 ** 31) - 1: return 0
    return ans

print(reverse(-123))