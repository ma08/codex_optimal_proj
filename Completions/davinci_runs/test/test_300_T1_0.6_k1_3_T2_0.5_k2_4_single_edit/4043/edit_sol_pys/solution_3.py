

import sys
import math
from collections import defaultdict
from heapq import *

def add_edge(graph, frm, to, cost=1):
    if frm == to: raise ValueError('invalid edge {}:{} -> {}'.format(cost, frm, to))
    graph[frm].append((to, cost))
    graph[to].append((frm, cost))

def readl():
    return map(int, sys.stdin.readline().split())

def dijkstra(graph, start, end):
    queue, enqueued = [(0, start, ())], set([start])
    while queue:
        (cost, v1, path) = heappop(queue)
        if v1 not in enqueued:
            enqueued.add(v1)
            path = (v1, path)
            if v1 == end:
                return (cost, path)

            for v2, c in graph[v1]:
                if v2 not in enqueued:
                    heappush(queue, (cost + c, v2, path))

    return float("inf")

def generate_graph(n, d, k):
    if d > n:
        return float("inf")

    if d == 1:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        else:
            return float("inf")

    if d == 2:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        elif k >= 2:
            return [1, 2]
        else:
            return float("inf")

    if d == 3:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        elif k >= 4:
            return [1, 2, 3, 3, 4, 5]
        else:
            return float("inf")

    if d == 4:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        elif k >= 3:
            return [1, 2, 3, 4, 5, 6]
        else:
            return float("inf")

    if k >= 4:
        return [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11]

    return float("inf")

def main():
    n, d, k = readl()
    graph = generate_graph(n, d, k)
    if graph == float("inf"):
        print "NO"
        sys.exit(0)

    print "YES"
    for i in range(1, n):
        print graph[i - 1], i

if __name__ == '__main__':
    main()
