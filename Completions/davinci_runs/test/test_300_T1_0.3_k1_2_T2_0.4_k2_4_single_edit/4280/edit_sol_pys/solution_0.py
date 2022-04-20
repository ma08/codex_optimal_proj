

def dfs(v, p):
    for u in g[v]:
        if u != p:
            dfs(u, v)
            c[v] += c[u]
