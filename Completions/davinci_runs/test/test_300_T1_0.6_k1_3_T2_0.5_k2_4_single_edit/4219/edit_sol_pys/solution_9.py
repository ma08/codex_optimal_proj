#!/usr/bin/env python3

import math
import sys

def dfs(v):
    global visited, honest, unkind, N
    visited[v] = True
    for i in range(N):
        if honest[v][i] == 1 and not visited[i]:
            dfs(i)
    for i in range(N):
        if unkind[v][i] == 1 and not visited[i]:
            dfs(i)

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
