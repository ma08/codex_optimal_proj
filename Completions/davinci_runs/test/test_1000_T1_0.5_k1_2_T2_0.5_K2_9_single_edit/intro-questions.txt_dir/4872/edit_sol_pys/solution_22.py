

from collections import defaultdict

n, m = [int(x) for x in input().split()]
d = defaultdict(list)

for i in range(n):
    a, b = [int(x) for x in input().split()]
    d[a].append(b)
    d[b].append(a)


print(d)
