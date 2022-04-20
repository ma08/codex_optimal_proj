

n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

def dfs(vertex, visited):
    global edges
    global n

    if len(visited) == n:
        return 1

    cnt = 0
    for edge in edges:
        if edge[0] == vertex and edge[1] not in visited:
            cnt += dfs(edge[1], visited + [vertex])
        elif edge[1] == vertex and edge[0] not in visited:
            cnt += dfs(edge[0], visited + [vertex])
    return cnt

print(dfs(1, []))