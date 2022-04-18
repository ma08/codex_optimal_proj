# coding: utf-8

import sys

n = int(input())
t = [int(input()) for i in range(n)]


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a
ans = t[0]

for i in t:
    ans = ans * i // gcd(ans, i)

print(ans)
