import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = input()

memo = {}

def f(n, s):
    if s in memo:
        return memo[s]
    if len(s) == 2*n:
        memo[s] = 1
    if len(s) > 2*n:
        memo[s] = 0
    if len(s) == 0:
        memo[s] = 1
    if len(s) == 1:
        memo[s] = 0
    if s[0] == '(' and s[-1] == ')': # 先頭と末尾が揃っている場合
        memo[s] = f(n, s[1:-1])
    if s[0] == ')':
        memo[s] = f(n, s[1:])
    if s[-1] == '(':
        memo[s] = f(n, s[:-1])
    memo[s] = f(n, s[1:]) + f(n, s[:-1])
    return memo[s]

print(f(n, s) % 1000000007)
