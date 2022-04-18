

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
a = []
for _ in range(N):
    T, A = map(int, input().split())
    a.append([T, A])

l = a[0][0]
r = a[0][1]
for i in range(1, N):
    l = lcm(l, a[i][0])
    r = lcm(r, a[i][1])

print(l+r)
