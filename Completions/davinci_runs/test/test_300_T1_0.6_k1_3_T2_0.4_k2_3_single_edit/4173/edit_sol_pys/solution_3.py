

import sys

def solve(n, a, b):
    return n * min(a, b) + n//2 * max(a, b)

q = int(raw_input().strip())
for a0 in xrange(q):
    n, a, b = raw_input().strip().split(' ')
    n, a, b = [int(n), int(a), int(b)]
    print solve(n, a, b)
