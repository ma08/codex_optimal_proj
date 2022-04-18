

import math
import sys

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
A = []
for _ in range(N):
    T, B = map(int, input().split())
    A.append([T, B])

l = A[0][0]
r = A[0][1]
for i in range(1, N):
    l = lcm(l, A[i][0])
    r = lcm(r, A[i][1])

print(l+r)
