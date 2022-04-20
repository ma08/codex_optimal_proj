

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append([a, b])

# print(edges)

graph = [[] for _ in range(N+1)]

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def dfs(graph, start, visited, path):
    path.append(start)

    if len(path) == N:
        print(path)
        return 1

    ret = 0
    for next in graph[start]:
        if not visited[next]:
            visited[next] = True
            ret += dfs(graph, next, visited, path)
            visited[next] = False
            path.pop()

    return ret

visited = [False for _ in range(N+1)]
visited[1] = True
print(dfs(graph, 1, visited, []))