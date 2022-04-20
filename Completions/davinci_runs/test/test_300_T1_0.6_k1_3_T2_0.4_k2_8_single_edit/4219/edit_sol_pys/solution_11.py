
import sys

def dfs(v):
    global visited, honest, unkind
    visited[v] = True
    for i in honest[v]:
        if not visited[i]:
            dfs(i)
    for i in unkind[v]:
        if not visited[i]:
            dfs(i)

N = int(input())
honest = [[] for i in range(N)]
unkind = [[] for i in range(N)]
for i in range(N):
    a_i = int(input())
    for j in range(a_i):
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
