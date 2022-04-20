

import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.adj = defaultdict(set)
        for u, v in edges:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def is_connected(self):
        visited = set()

        def dfs(u):
            visited.add(u)
            for v in self.adj[u]:
                if v not in visited:
                    dfs(v)

        dfs(1)
        return len(visited) == self.n

    def is_tree(self):
        return len(self.edges) == self.n - 1 and self.is_connected()

    def is_valid_degree(self, k):
        for u in range(1, self.n + 1):
            if len(self.adj[u]) > k:
                return False
        return True

    def is_valid_diameter(self, d):
        def dfs(u, p, path_len):
            nonlocal max_path_len
            max_path_len = max(max_path_len, path_len)
            for v in self.adj[u]:
                if v != p:
                    dfs(v, u, path_len + 1)

        max_path_len = 0
        dfs(1, None, 0)
        return max_path_len <= d


def main():
    n, d, k = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    g = Graph(n, edges)
    if g.is_tree() and g.is_valid_degree(k) and g.is_valid_diameter(d):
        print('YES')
        for u, v in g.edges:
            print(u, v)
    else:
        print('NO')


if __name__ == '__main__':
    main()