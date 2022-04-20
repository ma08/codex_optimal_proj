

import math
import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
x = list(map(int,sys.stdin.readline().rstrip().split()))

x.sort()

left = x[0] - 0
right = x[-1] - 0

ans = 0

for i in range(m):
    ans += min(abs(x[i] - left),abs(x[i] - right)) * 2
    left = min(left,x[i])
    right = max(right,x[i])

print(ans)
