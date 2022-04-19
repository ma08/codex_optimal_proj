

def dfs(v, p):
    for u in g[v]:
        if u != p:
            dfs(u, v)
            c[v] += c[u]

def dfs2(v, p, keep):
    mx = -1
    bigChild = -1
    for u in g[v]:
        if u != p and sz[u] > mx:
            mx = sz[u]
            bigChild = u
    for u in g[v]:
        if u != p and u != bigChild:
            dfs2(u, v, 0)
    if bigChild != -1:
        dfs2(bigChild, v, 1)
        c[bigChild] += c[v]
    if keep == 0:
        c[v] = 0

n, k = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

c = [1] * n
sz = [1] * n
dfs(0, -1)
dfs2(0, -1, 1)

ans = [0] * (n-1)
for i in range(n):
    for j in g[i]:
        if j > i:
            ans[i] = c[i]

print(max(ans))
print(' '.join(map(str, ans)))
