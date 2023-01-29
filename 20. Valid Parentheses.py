def isValid(s: str):
    lst = []
    dct = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i == "(" or i == "{" or i == "[": lst.append(i)
        elif len(lst) == 0 or lst[-1] != dct[i]: return False
        else: lst = lst[:-1]
    return False if len(lst) else True


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("]"))
