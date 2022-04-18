import sys
sys.setrecursionlimit(10**7)


def dfs(u):
    if u == 1:
        return 0
    if u in d:
        return d[u]

    d[u] = dfs(u-1) + 1
    if u % 2 == 0:
        d[u] = min(d[u], dfs(u//2) + 1)
    if u % 3 == 0:
        d[u] = min(d[u], dfs(u//3) + 1)

    return d[u]

n = int(input())
d = {1:0}

print(dfs(n))
