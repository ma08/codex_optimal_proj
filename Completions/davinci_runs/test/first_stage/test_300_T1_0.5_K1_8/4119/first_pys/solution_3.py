

import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

d = defaultdict(int)
for x in X:
    d[x] += 1

ans = 0
for k, v in d.items():
    ans += v - 1

print(ans)