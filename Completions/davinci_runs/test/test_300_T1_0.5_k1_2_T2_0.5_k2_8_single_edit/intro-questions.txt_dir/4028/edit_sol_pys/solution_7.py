import sys

n = int(input())
s = input()

memo = {}

    if s not in memo:
        if len(s) == 2*n:
            memo[s] = 1
        elif len(s) > 2*n:
            memo[s] = 0
        elif len(s) == 0:
            memo[s] = 1
        elif len(s) == 1:
            memo[s] = 0
        elif s[0] == '(' and s[-1] == ')':
            memo[s] = f(n, s[1:-1])
        elif s[0] == ')':
            memo[s] = f(n, s[1:])
        elif s[-1] == '(':
            memo[s] = f(n, s[:-1])
        else:
            memo[s] = f(n, s[1:]) + f(n, s[:-1])
def f(n, s):
    if s in memo:
        return memo[s]
    return memo[s]

print(f(n, s) % 1000000007)
