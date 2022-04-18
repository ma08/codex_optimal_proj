

import sys

#input
x, t = map(int, sys.stdin.readline().rstrip().split())

#calc
if t <= x - t: 
    ans = x - 2*t
else:
    ans = 2*t - x

#output
print(ans)
