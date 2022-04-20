

import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)
