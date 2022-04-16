

import math
import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
x = list(map(int,sys.stdin.readline().rstrip().split()))

x.sort()

ans = 0

for i in range(m):
    ans += x[i] - x[0]
    x[0] = x[i]

print(ans)
