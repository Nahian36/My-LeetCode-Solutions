def romanToInt(s: str):
    ans, dct = 0, {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s) - 1):
        if dct[s[i]] < dct[s[i + 1]]: ans -= dct[s[i]]
        else: ans += dct[s[i]]
    ans += dct[s[-1]]
    return ans


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("CM"))
print(romanToInt("LXXX"))
