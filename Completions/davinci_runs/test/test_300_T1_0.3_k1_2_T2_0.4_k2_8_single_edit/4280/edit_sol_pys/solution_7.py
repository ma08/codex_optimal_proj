
def dfs(start, parent):
    global n, k, edges, visited, colors
    visited[start] = True
    for edge in edges[start]:
        if edge == parent:
            continue
        if visited[edge]:
            k -= 1
        else:
            dfs(edge, start)
        else:
            k -= 1

n, k = map(int, input().split())
edges = [[] for _ in range(n)]
for i in range(n-1):
    x, y = map(int, input().split())
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)
visited = [False] * n
dfs(0, -1)
print(k+1)
print(' '.join(str(i % (k+1) + 1) for i in range(n-1)))
