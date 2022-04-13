from collections import defaultdict


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
    print(solve(n, a, tree))


if __name__ == "__main__":
    main()
