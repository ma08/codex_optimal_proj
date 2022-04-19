
n, k = map(int, input().split())  # noqa

def dfs(v, p):
    s = 1  # noqa
    for u in g[v]:
        if u == p:
            continue
        s += dfs(u, v)
    if s > k:  # noqa
        return 0  # noqa
    return s

g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dfs(0, -1)
print(k)
for i in range(n - 1):
    print(i % k + 1, end = ' ')
