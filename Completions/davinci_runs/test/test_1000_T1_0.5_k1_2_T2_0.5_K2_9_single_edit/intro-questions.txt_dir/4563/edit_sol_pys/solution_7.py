

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
A = [[0, 0] for _ in range(N)]
for _ in range(N):
    T, X = map(int, input().split())
    A[i][0] = T
    A[i][1] = X

l = A[0][0]
r = A[0][1]
for i in range(1, N):
    l = lcm(l, A[i][0])
    r = lcm(r, A[i][1])

print(l+r)
