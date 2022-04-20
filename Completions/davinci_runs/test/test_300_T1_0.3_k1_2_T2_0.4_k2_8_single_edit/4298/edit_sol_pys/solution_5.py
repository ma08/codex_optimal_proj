

import sys

N, D = map(int, sys.stdin.readline().split())

if N <= 2 * D:
    print(1)
else:
    print(2)
