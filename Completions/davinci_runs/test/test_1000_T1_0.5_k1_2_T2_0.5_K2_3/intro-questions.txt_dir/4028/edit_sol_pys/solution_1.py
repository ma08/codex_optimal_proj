n = int(input())
s = input()

memo = {
    '': 1,
    ')': 0,
    '(': 0,
}

def f(n, s):
    if s in memo or len(s) > 2*n:
        return 0
    if s[0] == '(' and s[-1] == ')':
        return f(n, s[1:-1])
    if s[0] == ')':
        return f(n, s[1:])
    if s[-1] == '(':
        return f(n, s[:-1])
    return f(n, s[1:]) + f(n, s[:-1])

print(f(n, s) % 1000000007)
