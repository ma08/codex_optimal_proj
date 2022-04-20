

n = int(input())
s = input()

memo = {}

def f(n, s):
    if s in memo:
        return memo[s]
        memo[s] = 1
    if len(s) == 2*n:
        return 1
        memo[s] = 0
    if len(s) > 2*n:
        return 0
    if len(s) == 0:
        memo[s] = 1
        return 1
    if len(s) == 1:
        memo[s] = 0
        return 0
    if s[0] == '(' and s[-1] == ')':
        memo[s] = f(n, s[1:-1])
        return memo[s]
    if s[0] == ')':
        memo[s] = f(n, s[1:])
        return memo[s]
    if s[-1] == '(':
        memo[s] = f(n, s[:-1])
        return memo[s]
    memo[s] = f(n, s[1:]) + f(n, s[:-1])
    return memo[s]

print(f(n, s) % 1000000007)
