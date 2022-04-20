
import sys


def solve(n, a, b, c):
    a, b = min(a, b), max(a, b)
    if a == b:
        return n * a
    if n % 2 == 0:
        return (a * (n//2)) + (b * (n//2))
    else:
        return (a * (n//2)) + (b * (n//2)) + a

q = int(raw_input().strip())
for a0 in xrange(q):
    n, a, b, c = raw_input().strip().split(' ')
    n, a, b, c = [int(n), int(a), int(b), int(c)]
    print solve(n, a, b, c)
