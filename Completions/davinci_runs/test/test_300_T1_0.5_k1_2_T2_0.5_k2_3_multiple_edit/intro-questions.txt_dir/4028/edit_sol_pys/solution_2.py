
n = int(input())
s = input()

memo = {'':1, ')':0, '(':0}

def f(n, s):
    if s in memo:
        return memo[s]
    if len(s) == 2*n and s.count('(') == n and s.count(')') == n:
        return 1
    if len(s) == 2*n: return 0
    if len(s) > 2*n: return 0
    if len(s) == 0: return memo[s]
    if len(s) == 1: return 0
    if s[0] == '(' and s[-1] == ')': return (f(n, s[1:-1]) + memo[s[1:-1]]) % 1000000007
    if s[0] == ')': return f(n, s[1:])
    if s[-1] == '(': return f(n, s[:-1])
    memo[s] = f(n, s[1:]) + f(n, s[:-1])
    return memo[s]

print(f(n, s))
