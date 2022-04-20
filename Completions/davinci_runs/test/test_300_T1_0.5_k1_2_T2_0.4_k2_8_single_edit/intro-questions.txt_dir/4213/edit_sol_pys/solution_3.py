

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dist = [-1] * N
dist[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for nv in graph[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = v
        q.append(nv)

if -1 in dist:
    print('No')
    exit()

print('Yes')
for d in dist[1:]:
    print(d+1)
