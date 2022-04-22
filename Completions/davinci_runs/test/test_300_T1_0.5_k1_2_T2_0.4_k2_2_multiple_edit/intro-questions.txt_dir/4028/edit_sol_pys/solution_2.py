
def f(n, s, memo, l):
    if n == 0:
        return 1
    if s in memo:
        return memo[s]
    if l == 2*n:
        memo[s] = 1
        return 1
    if l > 2*n:
        memo[s] = 0
        return 0
    if l == 0:
        memo[s] = 1
        return 1
    if l == 1:
        memo[s] = 0
        return 0
    if s[0] == '(' and s[-1] == ')':
        memo[s] = f(n-1, s[1:-1], memo, l-2)
        return memo[s]
    if s[0] == ')':
        memo[s] = f(n, s[1:], memo, l-1)
        return memo[s]
    if s[-1] == '(':
        memo[s] = f(n, s[:-1], memo, l-1)
        return memo[s]
    memo[s] = f(n, s[1:], memo, l-1) + f(n, s[:-1], memo, l-1)
    return memo[s]
for _ in range(int(input())):
    n = int(input())
    s = input()
    memo = {}
    print(f(n, s, memo, len(s)) % 1000000007)
