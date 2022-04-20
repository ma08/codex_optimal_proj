import sys
import math
n, x = map(int, sys.stdin.readline().split())


a = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(n):
    if a[i] > x:
        res += a[i] - x
        a[i] = x
    if a[i] < 0:
        res += -a[i]
        a[i] = 0

print(res)
