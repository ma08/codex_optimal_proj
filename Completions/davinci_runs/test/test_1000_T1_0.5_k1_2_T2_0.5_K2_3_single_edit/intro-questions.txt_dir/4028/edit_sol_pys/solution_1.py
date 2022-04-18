

memo = {}

def f(n, s):
    if s in memo:
        return memo[s]
    if len(s) == 2*n:
        return 1
    if len(s) > 2*n:
        return 0
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return 0
    if s[0] == '(' and s[-1] == ')': # 左右のみとばす
        return f(n, s[1:-1])
    if s[0] == ')': # 左のみとばす
        return f(n, s[1:])
    if s[-1] == '(': # 右のみとばす
        return f(n, s[:-1])
    return f(n, s[1:]) + f(n, s[:-1]) # 両方とばす

n = int(input())
s = input()
print(f(n, s))
