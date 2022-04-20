import sys

def dfs(v):
    global visited, honest, unkind
    visited[v] = True
    for i in range(len(honest[v])):
        if not visited[honest[v][i]]:
            dfs(honest[v][i])
    for i in range(len(unkind[v])):
        if not visited[unkind[v][i]]:
            dfs(unkind[v][i])

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
