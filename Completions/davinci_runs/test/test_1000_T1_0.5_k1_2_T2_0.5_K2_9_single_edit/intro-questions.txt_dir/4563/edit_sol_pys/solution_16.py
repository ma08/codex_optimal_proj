import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
B = []
for _ in range(N):
    t, a = map(int, input().split())
    B.append([t, a])

l = B[0][0]
r = B[0][1]
for i in range(1, N):
    l = lcm(l, B[i][0])
    r = lcm(r, B[i][1])

print(l+r)
