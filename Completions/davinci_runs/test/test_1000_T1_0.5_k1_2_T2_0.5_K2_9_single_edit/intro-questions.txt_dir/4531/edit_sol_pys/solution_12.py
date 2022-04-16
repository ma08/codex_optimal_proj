
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)


def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


class Tree:
    def __init__(self, n):
        self.visited = [False] * n
        self.n = n
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)


def solve(n, a, tree):
    res = 0
    for i in range(1, n + 1):
        res += tree.dfs(i, -1) * a[i]
    return res


def main():
    n = int(input())
    a = [0] + [int(x) for x in input().split()]
    tree = Tree(n)
    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        tree.add_edge(u, v)


if __name__ == "__main__":
    main()
