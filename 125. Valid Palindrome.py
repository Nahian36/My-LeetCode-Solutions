def isPalindrome(s: str):
    t = ''.join(filter(str.isalnum, s)).lower()
    return t == t[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))