def isMatch(s: str, p: str):
        arr, i = "", 0
        while i < len(p):
            if i < len(p) - 1 and len(arr) >= 2 and p[i + 1] == "*" and f'{p[i]}*' == arr[-2:]: i += 1
            else: arr += p[i]
            i += 1
        return __import__('re').fullmatch(arr, s) != None

print(isMatch(s = "aa", p = "a"))
print(isMatch(s = "aa", p = "a*a*"))
print(isMatch(s = "aa", p = "a*"))
print(isMatch(s = "ab", p = ".*"))
print(isMatch(s = "aaaaaaaaaaaaaaaaaaab", p = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"))