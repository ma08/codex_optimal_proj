

import sys
import numpy as np
from collections import defaultdict
import heapq

sys.setrecursionlimit(1000000)


def dijkstra(s, n, costs, edges):
    d = [float('inf')] * n
    d[s] = 0
    q = [(0, s)]
    while len(q) != 0:
        c, v = heapq.heappop(q)
        if d[v] < c:
            continue
        for u, cost in costs[v]:
            if d[u] > d[v] + cost:
                d[u] = d[v] + cost
                heapq.heappush(q, (d[u], u))
    return d


def main():
    n, m, s, t = map(int, input().split())
    s -= 1
    t -= 1
    costs = [[] for _ in range(n)]
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        a -= 1
        b -= 1
        costs[a].append((b, d))
        costs[b].append((a, d))
        edges[a].append(b)
        edges[b].append(a)

    d = dijkstra(s, n, costs, edges)
    print(d[t])


if __name__ == '__main__':
    main()
