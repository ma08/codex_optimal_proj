#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-11 22:50:34
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-11 22:50:34

import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.cost = [[float('inf') for _ in range(n)] for _ in range(n)]
        self.costs = set()
        self.is_edge = [[False for _ in range(n)] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))
        self.cost[u][v] = w
        self.cost[v][u] = w
        self.is_edge[u][v] = True
        self.is_edge[v][u] = True
        self.costs.add(w)

    def get_minimum_spanning_tree(self):
        visited = [False] * self.n
        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        total_cost = 0
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += weight
            for v, w in self.edges[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        return total_cost

    def get_minimum_cost(self):
        total_cost = self.get_minimum_spanning_tree()
        min_cost = min(self.costs) if self.costs else 0
        return total_cost + (self.n - 1) * min_cost

def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    graph = Graph(n)
    for _ in range(m):
        x, y, w = map(int, input().split())
        x -= 1
        y -= 1
        graph.add_edge(x, y, w)
    for i in range(n):
        for j in range(n):
            if not graph.is_edge[i][j]:
                graph.add_edge(i, j, a[i] + a[j])
    print(graph.get_minimum_cost())

if __name__ == '__main__':
    main()
