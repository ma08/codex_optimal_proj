

import math

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
t = [int(input()) for i in range(n)]

print(lcm(t[0], t[1]))
for i in range(2, n):
    print(lcm(lcm(t[0], t[1]), t[i]))