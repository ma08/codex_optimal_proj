

import math

A, B, K = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

gcd_val = gcd(A, B)

for i in range(K):
    if gcd_val % 2 == 0:
        gcd_val /= 2
    else:
        break

print(int(gcd_val))