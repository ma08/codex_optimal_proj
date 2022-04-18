
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
def get_graph(n, edges):
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append((edge[1], edge[2]))
        graph[edge[1]].append((edge[0], edge[2]))
    return graph
def dfs(graph, v, p, d):
    for nv, nd in graph[v]:
        if nv == p:
            continue
        d[nv] = max(d[v], nd)
        dfs(graph, nv, v, d)

def main():
    n, m = LI()
    edges = []
    for i in range(n-1):
        u, v, w = LI()
        edges.append((u-1, v-1, w))
    q = LI()

    uf = UnionFind(n)
    for u, v, w in edges:
        uf.union(u, v)

    d = [0] * n
    for u, v, w in edges:
        if uf.find(u) == uf.find(v):
            continue
        d[uf.find(u)] = max(d[uf.find(u)], w)
        d[uf.find(v)] = max(d[uf.find(v)], w)

    # graph = get_graph(n, edges)
    # dfs(graph, 0, -1, d)
    d.sort()

    for qi in q:
        ans = bisect.bisect_right(d, qi)
        print(ans, end=' ')
    print()

main()
