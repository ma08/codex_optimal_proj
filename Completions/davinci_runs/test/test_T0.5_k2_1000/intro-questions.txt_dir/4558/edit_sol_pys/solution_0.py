

import sys

#input
x, t = map(int, sys.stdin.readline().rstrip().split())

#calc
if t <= x - t:  # x - 2*t >= 0
    ans = x - 2*t
else:  # x - 2*t < 0
    ans = 2*t - x

#output
print(ans)
