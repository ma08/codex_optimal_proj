import sys

def dfs(v):
    global visited, honest, unkind
    visited[v] = True
    for u in honest[v]:
        if not visited[u]:
            dfs(u)
    for u in unkind[v]:
        if not visited[u]:
            dfs(u)

N = int(input())
honest = [[] for i in range(N)]
unkind = [[] for i in range(N)]
for i in range(N):
    A_i = int(input())
    for j in range(A_i):
        x, y = map(int, sys.stdin.readline().split())
        if y == 1:
            honest[i].append(x-1)
        else:
            unkind[i].append(x-1)
visited = [False] * N
ans = 0
for i in range(N):
    if visited[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
