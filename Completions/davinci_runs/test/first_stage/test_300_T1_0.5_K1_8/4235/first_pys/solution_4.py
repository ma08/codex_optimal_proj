

import sys

def dfs(v, p):
    for i in g[v]:
        if i != p:
            dfs(i, v)
    for i in g[v]:
        if i != p:
            for j in g[i]:
                if j != v:
                    g[v].append(j)

def dfs2(v, p):
    for i in g[v]:
        if i != p:
            dfs2(i, v)
            for j in g[i]:
                if j != v:
                    g[v].append(j)

n, m = map(int, input().split())
g = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1, 0)
dfs2(1, 0)

for i in range(1, n+1):
    if len(g[i]) != n-1:
        print("NO")
        sys.exit(0)

print("YES")
for i in range(1, n+1):
    for j in g[i]:
        if j > i:
            print(1, end="")
            break
    else:
        print(0, end="")
print()