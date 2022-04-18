

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)


class Tree:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, root, parent):
        children = self.adj[root]
        queue = deque()
        res = 0
        for c in children:
            if c != parent:
                queue.append(c)
        while queue:
            node = queue.popleft()
            res += self.bfs(node, root) + 1
        return res


def solve(n, a, tree):
    res = 0
    for i in range(1, n + 1):
        res += tree.bfs(i, -1) * a[i]
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
