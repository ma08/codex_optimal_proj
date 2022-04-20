

N, M = map(int, input().split())

edge = []
for i in range(M):
    edge.append(list(map(int, input().split())))


def dfs(graph, vertex, visited):
    if len(visited) == N:
        return 1

    ret = 0
    for next_vertex in graph[vertex]:
        if next_vertex not in visited:
            visited.add(next_vertex)
            ret += dfs(graph, next_vertex, visited)
            visited.remove(next_vertex)
    return ret


graph = [[] for _ in range(N + 1)]
for a, b in edge:
    graph[a].append(b)
    graph[b].append(a)

visited = {1}
print(dfs(graph, 1, visited))
