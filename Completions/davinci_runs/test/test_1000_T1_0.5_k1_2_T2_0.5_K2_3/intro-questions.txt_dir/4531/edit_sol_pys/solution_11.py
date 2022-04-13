import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


class Tree:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, parent, root):
        return sum(self.dfs(root, child) + 1 for child in self.adj[root] if child != parent)


def solve(n, a, tree):
    res = 0
    for i in range(1, n + 1):
        res += tree.dfs(-1, i) * a[i]
    return res


def main():
    n = int(input())
    a = [0] + [int(x) for x in input().split()]
    tree = Tree()
    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        tree.add_edge(u, v)
    print(solve(n, a, tree))


if __name__ == "__main__":
    main()
