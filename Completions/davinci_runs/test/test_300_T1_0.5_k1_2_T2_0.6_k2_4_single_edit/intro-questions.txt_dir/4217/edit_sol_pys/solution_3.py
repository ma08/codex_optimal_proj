#!/usr/bin/env python

from collections import deque


def bfs(s):
    """
    :param s: start node
    :return: None
    """
    d = [-1] * (N + 1)
    d[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for e in G[v]:
            if d[e] != -1:
                continue
            else:
                d[e] = d[v] + 1
                q.append(e)
    num = 0
    max_dist = 0
    for dist in d:
        if dist == 2:
            num += 1
        elif dist > max_dist:
            max_dist = dist
    print(num, max_dist)



G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
N, M = map(int, input().split())

bfs(1)
