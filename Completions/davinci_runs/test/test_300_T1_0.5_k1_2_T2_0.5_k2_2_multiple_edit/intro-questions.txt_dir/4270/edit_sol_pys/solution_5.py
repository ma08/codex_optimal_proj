from collections import defaultdict
from itertools import combinations

# N = int(input())
# A = list(map(int, input().split()))

N = 5
A = [1, 5, 3, 3, 2]

d = defaultdict(int)
for i in A:
    d[i] += 1

ans = 0
for k, v in d.items():
    if v >= k:
        ans += v - k
    else:
        ans += v

print(ans)
