n, k = map(int, input().split())

def dfs(v, p):
    global k
    s = 1
    for u in g[v]:
        if u == p:
            continue
        s += dfs(u, v)
    if s > k:
        k -= 1
        return 0
    return s

g = [[] for i in range(n)]
for i in range(n - 1):
    v, u = map(int, input().split())
    v -= 1
    u -= 1
    g[v].append(u)
    g[u].append(v)

dfs(0, -1)
print(k)
for i in range(n - 1):
    print(i % k + 1, end = ' ')
