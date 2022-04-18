#!/usr/bin/env python3


import heapq
import sys

# Read input and build graph
n, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    dna = sys.stdin.readline().strip()
    for j in range(i):
        u, v = i, j
        graph[u].append((v, sum(1 for a, b in zip(dna, graph[j][0][1]) if a != b)))
        graph[v].append((u, sum(1 for a, b in zip(dna, dna) if a != b)))

# Prim's algorithm
min_tree = []
min_weight = 0
visited = [False] * n
pq = [(0, 0, dna)]
while pq:
    weight, u, dna = heapq.heappop(pq)
    if not visited[u]:
        visited[u] = True
        min_tree.append((u, dna))
        min_weight += weight
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v, dna))

# Print results
print(min_weight)
for u, dna in min_tree[1:]:
    print(min_tree.index((u, dna)), u)
