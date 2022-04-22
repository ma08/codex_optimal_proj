
from collections import deque
n, m, s = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
s -= 1
d = [-1] * n
d[s] = 0
q = deque()
q.append(s)
while q:
    v = q.popleft()
    for u in g[v]:
        if d[u] == -1:
            d[u] = d[v] + 1
            q.append(u)
for i in range(n):
    print(d[i])
