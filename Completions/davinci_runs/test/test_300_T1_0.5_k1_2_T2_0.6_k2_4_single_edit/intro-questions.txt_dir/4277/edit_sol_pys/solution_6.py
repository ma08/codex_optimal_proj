

import sys

n, a, b = map(int, sys.stdin.readline().split())
if n*a > b:
    print(b)
else:
    print(n*a)
