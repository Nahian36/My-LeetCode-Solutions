def isPalindrome(x: int):
    if x < 0: return False
    elif x < 10: return True
    lst = list()
    while x > 0:
        mod = x % 10
        lst.append(int(mod))
        x = (x - mod) / 10
    lst.reverse()
    if lst[:int(len(lst) / 2)] == lst[-int(len(lst) / 2):][::-1]: return True
    else: return False

print(isPalindrome(1))