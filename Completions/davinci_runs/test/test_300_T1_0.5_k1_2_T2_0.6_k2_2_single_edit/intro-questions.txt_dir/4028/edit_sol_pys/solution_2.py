

n = int(input())
s = input()

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
    ret = 0
    if s[0] == '(':
        ret += f(n, s[1:])
    if s[-1] == ')':
        ret += f(n, s[:-1])
    memo[s] = ret
    return ret

print(f(n, s) % 1000000007)
