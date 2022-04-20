

import sys

n, m = map(int, sys.stdin.readline().split())

prefecture = [[] for _ in range(n + 1)]
for i in range(m):
    p, y = map(int, sys.stdin.readline().split())
    prefecture[p].append(y)

for i in range(n + 1):
    prefecture[i].sort()

for i in range(m):
    p, y = map(int, sys.stdin.readline().split())
    id = str(p).zfill(6) + str(prefecture[p].index(y) + 1).zfill(6)
    print(id)