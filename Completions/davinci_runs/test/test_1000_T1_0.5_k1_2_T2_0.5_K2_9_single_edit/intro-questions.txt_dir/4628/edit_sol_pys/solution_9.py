

import sys
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, start, end):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        queue = [start]
        while queue:
            current = queue.pop(0)
            if current == end:
                break
            for neighbor in self.graph[current]:
                distance = distances[current] + self.graph[current][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    queue.append(neighbor)
        return distances[end]


def solve(graph, routes):
    max_dist = 0
    for u, v in routes:
        d = graph.dijkstra(u, v)
        max_dist = max(max_dist, d)
    return max_dist


def main():
    n, m, k = map(int, sys.stdin.readline().strip().split())
    graph = Graph()
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        graph.add_edge(u, v, w)
    routes = []
    for _ in range(k):
        u, v = map(int, sys.stdin.readline().strip().split())
        routes.append((u, v))
    print(solve(graph, routes))


if __name__ == '__main__':
    main()
