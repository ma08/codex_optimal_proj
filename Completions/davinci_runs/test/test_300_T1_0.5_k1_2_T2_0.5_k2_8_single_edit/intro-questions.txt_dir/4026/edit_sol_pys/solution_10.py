from collections import defaultdict


n, m = [int(x) for x in input().split()]
d = defaultdict(int)
for i in range(n):
    d[input()] += 1

for i in range(m):
    print(d[input()])
