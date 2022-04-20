
import sys

def solve(n, m):
    if m == 1:
        return 2
    elif n == m:
        return 2 * n - 2
    else: 
        return n + m - 2

q = int(raw_input().strip())
for i in xrange(q):
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    print solve(n, m)
