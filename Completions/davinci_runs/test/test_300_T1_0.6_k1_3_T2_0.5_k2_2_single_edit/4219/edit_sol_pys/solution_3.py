import sys

def dfs(v):
    global visited, honest, unkind, N
    visited[v] = True
    for i in range(N):
        if honest[v][i] == 1 and not visited[i]:
            dfs(i)
        if unkind[v][i] == 1 and not visited[i]:
            dfs(i)

N = int(input())
honest = [[0] * N for i in range(N)]
unkind = [[0] * N for i in range(N)]
visited = [False] * N
for i in range(N):
    A_i = int(input())
    for j in range(A_i):
        x, y = map(int, sys.stdin.readline().split())
        if y == 0:
            honest[i][x-1] = 1
        elif y == 1:
            unkind[i][x-1] = 1
ans = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)
