import heapq

n, m, k = [int(x) for x in input().split()]
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y, w = [int(x) for x in input().split()]
    graph[x - 1].append((y - 1, w))
    graph[y - 1].append((x - 1, w))


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
                heapq.heappush(pq, (dist[v], v))

    return dist


dist = dijkstra(graph, 0)
dist.sort()

print(dist[k - 1])
