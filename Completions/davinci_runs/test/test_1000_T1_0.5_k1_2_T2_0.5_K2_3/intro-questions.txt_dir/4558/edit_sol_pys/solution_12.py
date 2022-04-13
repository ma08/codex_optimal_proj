
import sys

# input
x, t = map(int, sys.stdin.readline().rstrip().split())

# calculation
if t >= x:
    ans = 0
else:
    ans = x - t

# output
print(ans)
