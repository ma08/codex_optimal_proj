

import sys

#input
x, t = map(int, sys.stdin.readline().rstrip().split())

#calc
ans = max(x - 2*t, 0)

#output
print(ans)
