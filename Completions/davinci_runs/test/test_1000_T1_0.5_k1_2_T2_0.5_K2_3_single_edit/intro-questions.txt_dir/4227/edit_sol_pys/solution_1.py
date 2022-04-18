# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b)
    edges[b - 1].append(a)


def dfs(v, p):
    for i in edges[v]:
        if i == p:
            continue
        dfs(i, v)


dfs(0, -1)
