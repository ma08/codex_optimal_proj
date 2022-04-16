

import sys

#input
x, t = map(int, sys.stdin.readline().rstrip().split())

#calc
if t <= x:
    ans = x - t
else:
    ans = 0

#output
print(ans)
