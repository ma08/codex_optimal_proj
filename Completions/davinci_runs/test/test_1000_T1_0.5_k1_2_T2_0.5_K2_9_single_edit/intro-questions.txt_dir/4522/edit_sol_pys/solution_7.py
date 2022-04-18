

import sys
import os
import math
import collections
import heapq
import itertools
import array
import bisect
import copy

sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# def get_graph(n, edges):
#     graph = [[] for _ in range(n)]
#     for edge in edges:
#         graph[edge[0]].append((edge[1], edge[2]))
#         graph[edge[1]].append((edge[0], edge[2]))
#     return graph

# def dfs(graph, v, p, d):
#     for nv, nd in graph[v]:
#         if nv == p:
#             continue
#         d[nv] = max(d[v], nd)
#         dfs(graph, nv, v, d)

def main():
    n, m = LI()
    edges = []
    for i in range(n-1):
        u, v, w = LI()
        edges.append((u, v, w))
    q = LI()

    uf = UnionFind(n)
    for u, v, w in edges:
        uf.union(u-1, v-1)

    d = [0] * n
    for u, v, w in edges:
        if uf.find(u-1) == uf.find(v-1):
            continue
        d[uf.find(u-1)] = max(d[uf.find(u-1)], w)
        d[uf.find(v-1)] = max(d[uf.find(v-1)], w)

    # graph = get_graph(n, edges)
    # dfs(graph, 0, -1, d)
    d.sort()

    for qi in q:
        ans = bisect.bisect_right(d, qi)
        print(ans, end=' ')
    print()

main()
