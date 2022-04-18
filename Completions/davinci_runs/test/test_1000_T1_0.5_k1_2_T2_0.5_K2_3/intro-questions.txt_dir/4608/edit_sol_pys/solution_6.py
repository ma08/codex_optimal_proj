

import heapq
import sys


def dijkstra(start):
    d = [float('inf')] * N
    d[start] = 0
    que = [(0, start)]
    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist:
            continue
        for nv, nc in g[v]:
            if d[nv] > d[v] + nc:
                d[nv] = d[v] + nc
                heapq.heappush(que, (d[nv], nv))
    return d


def warshall_floyd(g):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    return g


def bellman_ford(start):
    d = [float('inf')] * N
    d[start] = 0
    for i in range(N):
        update = False
        for u in range(N):
            if d[u] == float('inf'):
                continue
            for v, cost in g[u]:
                if d[v] > d[u] + cost:
                    d[v] = d[u] + cost
                    update = True
        if not update:
            break
    return d


def kruskal():
    es = sorted(g, key=lambda x: x[2])
    uf = UnionFind(N)
    res = 0
    for e in es:
        if not uf.same(e[0], e[1]):
            uf.unite(e[0], e[1])
            res += e[2]
    return res


class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] == x:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.p[x] = y
        else:
            self.p[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

from collections import deque

N = int(input())
a = list(map(int, sys.stdin.read().split()))

g = [[] for _ in range(N)]
visited = [False] * N
queue = deque([1])


while len(queue) > 0:
    num = queue.popleft()
    if num == 2:
        print(visited[num]-1)
        sys.exit()
    if not visited[a[num-1]-1] and a[num-1] != num:
        visited[a[num-1]-1] = visited[num-1] + 1
        queue.append(a[num-1]-1)

print(-1)
