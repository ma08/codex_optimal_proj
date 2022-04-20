import collections

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
counter = collections.Counter(a)
ans = 0
for k, v in counter.items():
    if k > v:
        ans += v
    else:
        ans += v - k

print(ans)
