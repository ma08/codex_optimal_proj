
def dfs(start, parent):
    global n, k, edges, visited, color
    color[start] = k
    visited[start] = True
    for edge in edges[start]:
        if edge == parent:
            continue
        if not visited[edge]:
            k += 1
            dfs(edge, start)
        else:
            color[start] = min(color[start], color[edge])

n, k = map(int, input().split())
edges = [[] for _ in range(n)]
for i in range(n-1):
    x, y = map(int, input().split())
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)
visited = [False] * n
color = [0] * n
dfs(0, -1)
print(k)
print(' '.join(str(color[i]) for i in range(1, n)))
