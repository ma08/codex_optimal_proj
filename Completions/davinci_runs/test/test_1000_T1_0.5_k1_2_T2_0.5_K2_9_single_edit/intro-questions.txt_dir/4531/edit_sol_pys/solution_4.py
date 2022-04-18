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

    def dfs(self, root, parent):
        children = self.adj[root]
        res = 0
        for child in children:
            if child != parent:
                res += self.dfs(child, root) + 1
        return res


def solve(n, a, tree, root):
    res = 0
    children = tree.adj[root]
    for child in children:
        res += solve(n, a, tree, child) + a[child]
    return res


def main():
    n = int(input())
    a = [0] + [int(x) for x in input().split()]
    tree = Tree(n)
    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        tree.add_edge(u, v)
    print(solve(n, a, tree, 1))


if __name__ == "__main__":
    main()
