

import sys

n, k = map(int, sys.stdin.readline().split())
c = 1
p = list(map(int, sys.stdin.readline().split()))

for i in sorted(p)[:k]:
    print(i, end=" ")
