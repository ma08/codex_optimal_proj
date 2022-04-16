

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
A = [0] * N
for _ in range(N):
    T, A[_] = map(int, input().split())

l = A[0]
r = A[0]
for i in range(1, N):
    l = lcm(l, A[i])
    r = lcm(r, A[i])

print(l+r)
