

# Solution

import math
import sys
input = sys.stdin.readline


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) // gcd(a, b)


n = int(input())
a = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = min(ans, lcm(a[i], a[j]))

for i in range(n - 1):
    for j in range(i + 1, n):
        if lcm(a[i], a[j]) == ans:
            print(i + 1, j + 1)
            exit(0)