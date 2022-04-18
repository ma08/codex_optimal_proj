

n, m = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    print(len(graph[i]))
