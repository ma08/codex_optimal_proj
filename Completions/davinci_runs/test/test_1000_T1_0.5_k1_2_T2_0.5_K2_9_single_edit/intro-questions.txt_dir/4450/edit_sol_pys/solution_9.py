
n, m, k = [int(x) for x in input().split()]

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, w = [int(x) for x in input().split()]
    graph[a - 1].append((b - 1, w))
    graph[b - 1].append((a - 1, w))


def dijkstra(graph, source):
    dist = [float('inf')] * n
    visited = [False] * n
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heappush(pq, (dist[v], v))

    return dist


dist = dijkstra(graph, 0)
dist.sort()

print(dist[k - 1])
