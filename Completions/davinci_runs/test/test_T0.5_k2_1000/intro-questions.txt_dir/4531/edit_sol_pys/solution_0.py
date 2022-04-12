import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


class Tree:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, root):
        pass


def solve(n, a, tree):
    pass


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    tree = Tree(n)
    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        tree.add_edge(u, v)
    print(solve(n, a, tree))


if __name__ == "__main__":
    main()
