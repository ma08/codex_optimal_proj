

import sys

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

n = int(input())
a = list(map(int, input().split()))

min_lcm = lcm(a[0], a[1])
min_lcm_pair = (1, 2)

for i in range(n):
    for j in range(i+1, n):
        l = lcm(a[i], a[j])
        if l < min_lcm:
            min_lcm = l
            min_lcm_pair = (i+1, j+1)

print(min_lcm_pair[0], min_lcm_pair[1])