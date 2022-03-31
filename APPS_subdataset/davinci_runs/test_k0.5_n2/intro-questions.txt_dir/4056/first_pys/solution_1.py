

import sys
import math

# sys.stdin = open('input.txt', 'r')

n = int(input())
a = list(map(int, input().split()))

gcd = a[0]
for i in range(1, n):
    gcd = math.gcd(gcd, a[i])

cnt = 0
for i in range(1, math.ceil(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        cnt += 1
    if i * i != gcd:
        cnt += 1

print(cnt)