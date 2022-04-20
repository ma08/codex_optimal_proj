

import sys
import math
import heapq
import itertools
import collections

class Graph:
    def __init__(self, n):
        self.nodes = n
        self.edges = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

def dfs(g, start, visited):
    visited[start] = True

    for v in g.edges[start]:
        if visited[v] == False:
            dfs(g, v, visited)

def main():
    n, k = [int(x) for x in input().split()]
    g = Graph(n)

    for i in range(n-1):
        x, y = [int(x) for x in input().split()]
        g.add_edge(x, y)

    visited = [False] * n
    dfs(g, 1, visited)

    if False in visited:
        print("Graph is not connected")
    else:
        print("Graph is connected")

if __name__ == "__main__":
    main()