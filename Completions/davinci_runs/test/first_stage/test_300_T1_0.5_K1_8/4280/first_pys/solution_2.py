

def dfs(u):
    global color,n,k
    color[u] = 1
    for v in g[u]:
        if color[v] == 0:
            dfs(v)
            if color[v] == 1:
                color[u] = 2

n,k = map(int,input().split())
g = [[] for i in range(n+1)]
color = [0]*(n+1)
for i in range(n-1):
    x,y = map(int,input().split())
    g[x].append(y)
    g[y].append(x)
dfs(1)
c = 0
for i in range(1,n+1):
    if color[i] == 2:
        c+=1
if c > k:
    print("-1")
else:
    print(c)
    ans = [0]*(n-1)
    stack = [1]
    c = 1
    while stack:
        u = stack.pop()
        for v in g[u]:
            if color[v] == 1:
                ans[v-1] = c
                stack.append(v)
        if color[u] == 2:
            c+=1
    print(*ans)