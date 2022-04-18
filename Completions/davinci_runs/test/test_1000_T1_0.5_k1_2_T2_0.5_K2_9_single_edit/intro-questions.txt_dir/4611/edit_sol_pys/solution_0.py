from collections import deque

def bfs(v):
    d = [-1]*n
    d[v] = 0
    q = deque([v])
    while q:
        v = q.popleft()
        for e in edges[v]:
            if d[e] != -1:
                continue
            d[e] = d[v] + 1
            q.append(e)
    return d


n = int(input())

edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

d = bfs(0)

for i in range(n):
    if abs(x[i]-x[i-1]) + abs(y[i]-y[i-1]) > t[i]-t[i-1]:
        print('No')
        exit()
    if (t[i]-t[i-1])%2 != (abs(x[i]-x[i-1]) + abs(y[i]-y[i-1]))%2:
        print('No')
        exit()

print('Yes')
