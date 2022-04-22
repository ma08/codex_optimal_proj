n = int(input())
S = input()


def f(n, S):
    if len(S) == 2*n:
        return 1
    if len(S) > 2*n:
        return 0
    if len(S) == 0:
        return 1
    if len(S) == 1:
        return 0
    if S[0] == '(' and S[-1] == ')':
        return f(n, S[1:-1])
    if S[0] == ')':
        return f(n, S[1:])
    if S[-1] == '(':
        return f(n, S[:-1])
    return f(n, S[1:]) + f(n, S[:-1])

print(f(n, s) % 1000000007)
