def lengthOfLastWord(s: str):
    count, ans = 0, 0
    for i in s:
        if i != " ": count += 1
        elif count > 0: ans, count = count, 0
    if count > 0: ans = count 
    return ans


print(lengthOfLastWord("Today is a nice day"))
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))