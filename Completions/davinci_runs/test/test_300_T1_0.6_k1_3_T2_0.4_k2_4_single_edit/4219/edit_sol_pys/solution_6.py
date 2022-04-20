# coding: utf-8

import sys

def dfs(v):
    global visited, honest, unkind, N
    visited[v] = True
    for i in range(N):
        if honest[v][i] and not visited[i]:
            dfs(i)
    for i in range(N):
        if unkind[v][i] and not visited[i]:
            dfs(i)

N = int(input())
honest = [[False] * N for i in range(N)]
unkind = [[False] * N for i in range(N)]
for i in range(N):
    A_i = int(input())
    for j in range(A_i):
        x, y = map(int, sys.stdin.readline().split())
        if y == 1:
            honest[i][x-1] = True
        else:
            unkind[i][x-1] = True
visited = [False] * N
ans = 0
for i in range(N):
    if visited[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
