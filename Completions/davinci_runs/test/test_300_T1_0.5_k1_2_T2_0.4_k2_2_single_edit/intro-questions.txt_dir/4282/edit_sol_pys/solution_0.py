
from collections import defaultdict

n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

d = defaultdict(list)
for i in range(1, n + 1):
    d[a[i]].append(i)

for i in range(1, n + 1):
    if len(d[b[i]]) > 0:
        print(d[b[i]][0])
        d[b[i]].pop(0)
    else:
        print(-1)
