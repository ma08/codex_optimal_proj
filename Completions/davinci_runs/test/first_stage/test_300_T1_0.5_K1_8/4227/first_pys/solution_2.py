

n, m = map(int, input().split())
path = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)


def dfs(v, visited, path, count):
    visited[v] = True
    count += 1
    if count == n:
        return 1
    ret = 0
    for i in path[v]:
        if not visited[i]:
            ret += dfs(i, visited, path, count)
    visited[v] = False
    return ret


visited = [False for i in range(n)]
print(dfs(0, visited, path, 0))