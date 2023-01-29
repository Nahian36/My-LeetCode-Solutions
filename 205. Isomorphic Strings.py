def isIsomorphic(s: str, t: str):
    dct, ans = {}, ""
    for i in range(len(s)):
        if t[i] not in dct.values(): dct[s[i]] = t[i]
        elif (s[i] not in dct) or (dct[s[i]] != t[i]): return False
    for i in range(len(s)): ans += dct[s[i]]
    return ans == t

print(isIsomorphic(s = "egg", t = "add"))
print(isIsomorphic(s = "foo", t = "bar"))
print(isIsomorphic(s = "paper", t = "title"))
print(isIsomorphic(s = "badc", t = "baba"))