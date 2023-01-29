
def generateParenthesis(n: int):
    def gen(n,  l,  r,  s, ans):
        if l == n and r == n:
            ans.append(s)
            return
        if l < n: gen(n, l+1, r, s+"(", ans)
        if r < l: gen(n, l, r + 1, s+")", ans)
    ans = []
    gen(n, 0, 0, "", ans)
    return ans
    
print(generateParenthesis(3))
print(generateParenthesis(6))
