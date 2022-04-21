#include <bits/stdc++.h>

n = int(input())
s = input()

#define P pair<int, int>

unordered_map<string, int> memo;

def f(n, s):
    if s in memo:
        return memo[s]
    if len(s) == 2*n:
        return 1
    if len(s) > 2*n:
        return 0
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return 0
    if s[0] == '(' && s[-1] == ')':
        return f(n, s[1:-1])
    if s[0] == ')':
        return f(n, s[1:])
    if s[-1] == '(':
        return f(n, s[:-1])
    return f(n, s[1:]) + f(n, s[:-1])

print(f(n, s) % 1000000007)
