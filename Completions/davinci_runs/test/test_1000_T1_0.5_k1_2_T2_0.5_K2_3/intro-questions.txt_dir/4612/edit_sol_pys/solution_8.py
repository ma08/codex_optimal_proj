# coding: utf-8

import sys
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(edges, start):
    d = defaultdict(lambda: float('inf'))
    d[start] = 0
    q = [(0, start)]
    while q:
        w, v = heappop(q)
        if d[v] < w:
            continue
        for v2, w2 in edges[v]:
            if d[v2] > w + w2:
                d[v2] = w + w2
                heappush(q, (w + w2, v2))
    return d


def main():
    n, m, s, t = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        edges[u].append((v, a))
        edges[v].append((u, a))
        edges[u].append((v, b))
        edges[v].append((u, b))
    d = dijkstra(edges, s)
    print(d[t])


def _test():
    from random import randint
    from time import time
    from heapq import heappush, heappop
    from collections import defaultdict
    sys.setrecursionlimit(10 ** 9)
    INF = float('inf')
    MOD = 10 ** 9 + 7

    def dijkstra(edges, start):
        d = defaultdict(lambda: float('inf'))
        d[start] = 0
        q = [(0, start)]
        while q:
            w, v = heappop(q)
            if d[v] < w:
                continue
            for v2, w2 in edges[v]:
                if d[v2] > w + w2:
                    d[v2] = w + w2
                    heappush(q, (w + w2, v2))
        return d

    def gen_random_graph(n, m, cmin, cmax):
        edges = defaultdict(list)
        for _ in range(m):
            u = randint(0, n - 1)
            v = randint(0, n - 1)
            c1 = randint(cmin, cmax)
            c2 = randint(cmin, cmax)
            edges[u].append((v, c1))
            edges[v].append((u, c1))
            edges[u].append((v, c2))
            edges[v].append((u, c2))
        return edges

    N = 10 ** 5
    M = 10 ** 5
    CMAX = 10 ** 9
    for _ in range(10):
        edges = gen_random_graph(N, M, 0, CMAX)
        start = randint(0, N - 1)
        t = time()
        dijkstra(edges, start)
        print(time() - t)


if __name__ == '__main__':
    main()
