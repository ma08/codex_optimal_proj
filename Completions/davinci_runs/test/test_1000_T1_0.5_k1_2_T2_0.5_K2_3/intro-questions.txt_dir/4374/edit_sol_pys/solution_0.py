#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import heappop, heappush

def tree_diameter(edges):
    """
    Given a list of edges, return the tree diameter
    """
    # Create graph from edges
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    # Dijkstra from any node to find the farthest node
    start = next(iter(graph))
    queue = [(0, start)]
    dist = {}
    while queue:
        d, node = heappop(queue)
        if node not in dist:
            dist[node] = d
            for n in graph[node]:
                heappush(queue, (d+1, n))

    # Dijkstra from the farthest node to find the farthest node again
    start = max(dist, key=dist.get)
    queue = [(0, start)]
    dist = {}
    while queue:
        d, node = heappop(queue)
        if node not in dist:
            dist[node] = d
            for n in graph[node]:
                heappush(queue, (d+1, n))

    # The diameter is the maximum distance we found
    return max(dist.values())


def main():
    """
    Main function
    """
    # Get input
    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    edges = []
    for _ in range(m):
        a, b = [int(x) for x in sys.stdin.readline().strip().split()][:2]
        edges.append((a, b))

    # Get diameter
    diameter = tree_diameter(edges)

    # Print diameter
    print(diameter)

    # Add edges if possible
    if m < n - 1:
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if (i, j) not in edges:
                    print(i, j)

if __name__ == "__main__":
    main()
