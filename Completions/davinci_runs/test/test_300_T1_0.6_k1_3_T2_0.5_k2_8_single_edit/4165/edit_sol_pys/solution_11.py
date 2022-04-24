

import heapq
import math
import sys

inf = float("inf")

class Graph:
    def __init__(self):
        self.graph = {}
        self.dist = {}

    def add_edge(self, u, v, w):
        if u in self.graph:
            self.graph[u][v] = w
        else:
            self.graph[u] = {v: w}

    def dijkstra(self, s):
        self.dist[s] = 0
        pq = []
        heapq.heappush(pq, (0, s))

        while pq:
            d, u = heapq.heappop(pq)
            if d > self.dist[u]:
                continue
            for v, w in self.graph[u].items():
                if v not in self.dist or self.dist[v] > self.dist[u] + w:
                    self.dist[v] = self.dist[u] + w
                    heapq.heappush(pq, (self.dist[v], v))

    def shortest_path(self, s, t):
        self.dijkstra(s)
        return self.dist[t]

    def all_shortest_path(self, s):
        self.dijkstra(s)
        return self.dist


def main():
    n, m = map(int, sys.stdin.readline().split())
    g = Graph()
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        g.add_edge(u, v, w)
        g.add_edge(v, u, w)

    s, t = map(int, sys.stdin.readline().split())
    print(g.shortest_path(s, t))


if __name__ == "__main__":
    main()
