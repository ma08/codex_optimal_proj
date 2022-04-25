
n = int(input()) # количество вершин
m = int(input()) # количество ребер

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
