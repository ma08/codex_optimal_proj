

import sys
import os
from collections import defaultdict
from heapq import *

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
        self.edges = []

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.append((u, v, w))

    def prim(self, start):
        visited = set()
        visited.add(start)
        heap = []
        for v, w in self.graph[start]:
            heappush(heap, (w, v))
        mst = []
        while heap:
            weight, v = heappop(heap)
            if v not in visited:
                visited.add(v)
                mst.append((start, v, weight))
                for v_, w_ in self.graph[v]:
                    if v_ not in visited:
                        heappush(heap, (w_, v_))
        return mst

    def kruskal(self):
        self.edges.sort(key=lambda x: x[2])
        mst = []
        for u, v, w in self.edges:
            if u not in self.vertices or v not in self.vertices:
                continue
            self.vertices.remove(u)
            self.vertices.remove(v)
            mst.append((u, v, w))
            if len(self.vertices) == 0:
                break
        return mst


def main():
    n, m, k = map(int, sys.stdin.readline().strip().split())
    g = Graph()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        g.add_edge(u, v, 1)
    mst = g.kruskal()
    #print(mst)

    mst_edges = set()
    for u, v, w in mst:
        mst_edges.add((u, v))
        mst_edges.add((v, u))

    for u, v, w in g.edges:
        if (u, v) in mst_edges:
            print(0, end='')
        else:
            print(1, end='')
    print()


if __name__ == '__main__':
    main()