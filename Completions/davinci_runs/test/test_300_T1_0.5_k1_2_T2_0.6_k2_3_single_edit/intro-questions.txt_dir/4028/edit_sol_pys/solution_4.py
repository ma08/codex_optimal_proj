

def f(n, s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if s[0] == '(' and s[-1] == ')':
        return f(n, s[1:-1])
    if s[0] == ')':
        return f(n, s[1:])
    if s[-1] == '(':
        return f(n, s[:-1])
    return f(n, s[1:]) + f(n, s[:-1])

print(f(int(input()),input()))
