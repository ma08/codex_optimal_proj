
import sys

#input
x, t = map(int, sys.stdin.readline().rstrip().split())

#calc
if t <= x - t: # x - 2t >= 0
    ans = x - 2*t # x - 2t
else:
    ans = 0

#output
print(ans)
