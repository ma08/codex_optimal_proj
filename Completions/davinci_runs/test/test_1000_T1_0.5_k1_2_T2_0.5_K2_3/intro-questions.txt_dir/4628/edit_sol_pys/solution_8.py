#!/usr/bin/python3

import sys
from collections import defaultdict

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    graph = defaultdict(dict)
    for i in range(m):
        x, y, w = map(int, sys.stdin.readline().split())
        graph[x][y] = w
        graph[y][x] = w
    routes = []  # routes to be checked
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        routes.append((a, b))
    print(solve(graph, routes))

def solve(graph, routes):
    max_dist = 0
    for r1, r2 in routes:
        d = shortest_path(graph, r1, r2)
        max_dist = max(max_dist, d)
    return max_dist

def shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
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
