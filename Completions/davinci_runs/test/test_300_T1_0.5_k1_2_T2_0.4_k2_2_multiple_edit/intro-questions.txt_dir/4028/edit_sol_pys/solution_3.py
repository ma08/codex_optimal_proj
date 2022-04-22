def f(n, s, memo):
    if n == 0:
        return 1
    if s in memo:
        return memo[s]
    if len(s) == 2*n:
        memo[s] = 1
        return 1
    if len(s) > 2*n:
        memo[s] = 0
        return 0
    if len(s) == 0:
        memo[s] = 1
        return 1
    if len(s) == 1:
        memo[s] = 0
        return 0
    if s[0] == '(' and s[-1] == ')':
        memo[s] = f(n-1, s[1:-1], memo)
        return memo[s]
    if s[0] == ')':
        memo[s] = f(n, s[1:], memo)
        return memo[s]
    if s[-1] == '(':
        memo[s] = f(n, s[:-1], memo)
        return memo[s]
    memo[s] = f(n, s[1:], memo) + f(n, s[:-1], memo)
    return memo[s]


for _ in range(int(input())):
    n = int(input())
    s = input()
    memo = {}
    print(f(n, s, memo) % 1000000007)
