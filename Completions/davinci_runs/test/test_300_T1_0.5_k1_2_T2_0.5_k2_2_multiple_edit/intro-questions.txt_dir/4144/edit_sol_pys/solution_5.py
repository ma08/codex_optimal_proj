import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, -c))

INF = 10**18
dist = [INF] * N
dist[0] = 0


q = []
heapq.heappush(q, (0, 0))
while q:
    d, v = heapq.heappop(q)
    if dist[v] < d:
        continue
    for nv, nd in graph[v]:
        nd += d
        if dist[nv] > nd:
            dist[nv] = nd
            heapq.heappush(q, (nd, nv))


print(-dist[N - 1])
