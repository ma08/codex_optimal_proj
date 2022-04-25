from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

d = [-1 for i in range(n)]
q = deque()
q.append(0)
d[0] = 0
while len(q) > 0:
    v = q.popleft()
    for u in a[v]:
        if d[u] != -1:
            continue
        d[u] = d[v] + 1
        q.append(u)

for i in range(n):
    print(d[i])
