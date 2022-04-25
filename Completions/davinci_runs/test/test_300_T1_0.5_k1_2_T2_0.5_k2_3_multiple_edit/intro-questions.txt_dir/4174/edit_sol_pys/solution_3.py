
import sys, math

n, k = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
a.sort()
l = 0
r = n - 1
cnt = 0

while l < r:
    if a[l] + a[r] < k:
        cnt += r - l
        l += 1
    else:
        r -= 1

print(cnt)
