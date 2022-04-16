

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
A = []
for _ in range(N):
    T, A = map(int, input().split()) # T = time, A = amount
    A.append([T, A])

l = A[0][0] # time
r = A[0][1] # amount
for i in range(1, N):
    l = lcm(l, A[i][0])
    r = lcm(r, A[i][1])

print(l+r)
