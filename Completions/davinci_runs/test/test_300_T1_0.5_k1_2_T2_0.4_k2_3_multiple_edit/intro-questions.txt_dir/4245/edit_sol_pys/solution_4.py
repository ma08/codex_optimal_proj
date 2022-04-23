from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

d = deque()
d.append(1)
visited[1] = True

while d:
    v = d.popleft()
    for i in graph[v]:
        if not visited[i]:
            d.append(i)
            visited[i] = True

print(visited.count(True) - 1)
