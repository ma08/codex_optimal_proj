

import sys
from math import ceil

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

left = 0
right = 10**18

while right - left > 1:
    mid = (left + right) // 2
    cnt = 0
    for i in range(n):
        cnt += ceil(a[i] / mid) - 1
    if cnt <= m:
        right = mid
    else:
        left = mid

print(right)
