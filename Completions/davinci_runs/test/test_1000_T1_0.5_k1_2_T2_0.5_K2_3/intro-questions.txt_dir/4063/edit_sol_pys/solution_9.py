
from itertools import accumulate

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a = list(accumulate(a))

if a[-1] < m:
    print(0)
    exit()

l, r = 0, n-1
while l < r:
    mid = (l+r+1) // 2
    if a[mid] < m:
        l = mid
    else:
        r = mid-1

print(n-l)
