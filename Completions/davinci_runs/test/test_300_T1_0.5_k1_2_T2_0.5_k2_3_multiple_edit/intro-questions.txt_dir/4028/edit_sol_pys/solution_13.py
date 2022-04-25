#
# n = int(input())
# s = input()
#
# memo = {'':1}
#
# def f(n, s):
#     if len(s) == 2*n:
#         return memo[s]
#     if len(s) > 2*n:
#         return 0
#     if len(s) == 0:
#         return memo[s]
#     if len(s) == 1:
#         return 0
#     if s[0] == '(' and s[-1] == ')':
#         return (f(n, s[1:-1]) + memo[s[1:-1]]) % 1000000007
#     if s[0] == ')':
#         return f(n, s[1:])
#     if s[-1] == '(':
#         return f(n, s[:-1])
#     return f(n, s[1:]) + f(n, s[:-1])
#
# for i in range(2*n):
#     memo[s[:i]] = f(n, s[:i])
#
# print(f(n, s) % 1000000007)
