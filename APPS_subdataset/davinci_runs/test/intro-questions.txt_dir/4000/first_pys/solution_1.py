

# Solution

import queue

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def bfs(graph, start):
    dist = [None for i in graph]
    dist[start] = 0
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        cur = q.get()
        for neighbor in graph[cur]:
            if dist[neighbor] is None:
                dist[neighbor] = dist[cur] + 1
                q.put(neighbor)
    return dist

dist_from_1 = bfs(graph, 0)
max_vertex = 0
for i in range(1, N):
    if dist_from_1[i] > dist_from_1[max_vertex]:
        max_vertex = i

a = 0
b = max_vertex
dist_from_b = bfs(graph, max_vertex)
max_vertex = 0
for i in range(1, N):
    if dist_from_b[i] > dist_from_b[max_vertex]:
        max_vertex = i
c = max_vertex

res = dist_from_1[b] + dist_from_b[c]
print(res)
print(a + 1, b + 1, c + 1)