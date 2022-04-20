

import math
import sys

n = int(input())
v = list(map(int, input().split()))

counts = {}
for i in range(n):
    if v[i] in counts:
        counts[v[i]] += 1
    else:
        counts[v[i]] = 1

if len(counts) > 2:
    print(-1)
    sys.exit()

if len(counts) == 2:
    print(math.min(counts[list(counts.keys())[0]], counts[list(counts.keys())[1]]))
    sys.exit()

print(counts[list(counts.keys())[0]] - 2)
