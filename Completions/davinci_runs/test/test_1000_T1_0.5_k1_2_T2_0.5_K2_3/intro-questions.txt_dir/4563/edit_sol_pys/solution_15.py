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
    T, a = map(int, input().split())
    A.append([T, a])

l = A[0][0]
r = A[0][1]
for i in range(1, N):
    l = lcm(l, A[i][0])
    r = lcm(r, A[i][1])

print(l+r)
