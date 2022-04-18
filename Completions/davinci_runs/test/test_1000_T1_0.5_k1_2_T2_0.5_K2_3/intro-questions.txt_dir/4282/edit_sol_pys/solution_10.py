from collections import defaultdict
from heapq import *

n = int(input())
s = input()

d = defaultdict(int)
for i in range(n):
    d[s[i]] += 1

q = []
for k, v in d.items():
    heappush(q, (-v, k))

res = ''
while len(q) > 1:
    c1, k1 = heappop(q)
    c2, k2 = heappop(q)
    res += k1 + k2
    if c1 + 1:
        heappush(q, (c1 + 1, k1))
    if c2 + 1:
        heappush(q, (c2 + 1, k2))
if q:
    c, k = heappop(q)
    if -c == 1:
        res += k
    else:
        print('NO SOLUTION')
        exit()
print(res)
