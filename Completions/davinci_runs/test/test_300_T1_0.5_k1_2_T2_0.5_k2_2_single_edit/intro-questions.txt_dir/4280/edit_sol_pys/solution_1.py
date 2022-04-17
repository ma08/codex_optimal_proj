
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
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

dfs(0, -1)
print(k)
for i in range(n - 1):
    print(i % k + 1, end = ' ')
