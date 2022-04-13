#!/usr/bin/env python

import sys
from collections import defaultdict

def main():
    n, m, k = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(dict)
    for i in range(m):
        x, y, w = map(int, sys.stdin.readline().strip().split())
        graph[x][y] = w
        graph[y][x] = w
    routes = []
    for i in range(k):
        a, b = map(int, sys.stdin.readline().strip().split())
        routes.append((a, b))
    print(solve(graph, routes))

def solve(graph, routes):
    max_dist = 0
    for r1, r2 in routes:
        d = dijkstra(graph, r1, r2)
        max_dist = max(max_dist, d)
    return max_dist

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph.keys()}
    distances[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in graph[current]:
            distance = distances[current] + graph[current][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append(neighbor)
    return distances[end]

if __name__ == '__main__':
    main()
