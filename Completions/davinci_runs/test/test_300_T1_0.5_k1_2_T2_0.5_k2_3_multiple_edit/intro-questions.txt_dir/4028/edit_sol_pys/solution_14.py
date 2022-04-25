import sys
sys.setrecursionlimit(10**7)

n = int(input())
s = input()

memo = {}

def f(n, s):
    if s in memo:
        return memo[s]
    if len(s) == 2*n:
        return 1 % 1000000007
    if len(s) > 2*n:
        return 0
    if len(s) == 0:
        return 1 % 1000000007
    if len(s) == 1:
        return 0
    if s[0] == '(' and s[-1] == ')' and len(s) > 2:
        return f(n, s[1:-1]) % 1000000007
    if s[0] == ')':
        return f(n, s[1:]) % 1000000007
    if s[-1] == '(':
        return f(n, s[:-1]) % 1000000007
    memo[s] = (f(n, s[1:]) + f(n, s[:-1])) % 1000000007
    return memo[s]

print(f(n, s) % 1000000007)
