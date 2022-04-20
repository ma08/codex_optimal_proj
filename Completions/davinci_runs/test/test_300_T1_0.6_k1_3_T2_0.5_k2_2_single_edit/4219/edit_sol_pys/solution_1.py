# -*- coding: utf-8 -*-

import sys

def dfs(v):
    global visited, honest, dishonest
    visited[v] = True
    for i in range(len(honest[v])):
        if not visited[honest[v][i]]:
            dfs(honest[v][i])
    for i in range(len(dishonest[v])):
        if not visited[dishonest[v][i]]:
            dfs(dishonest[v][i])

N = int(input())
honest = [[] for i in range(N)]
dishonest = [[] for i in range(N)]
for i in range(N):
    A_i = int(input())
    for j in range(A_i):
        x, y = map(int, sys.stdin.readline().split())
        if y == 1:
            honest[i].append(x-1)
        else:
            dishonest[i].append(x-1)
visited = [False] * N
ans = 0
for i in range(N):
    if visited[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
