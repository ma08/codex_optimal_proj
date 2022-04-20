

import sys


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, v, p=-1):
        for u in self.adj[v]:
            if u != p:
                self.dfs(u, v)

    def check(self, v, p=-1):
        if len(self.adj[v]) > 2:
            return False
        for u in self.adj[v]:
            if u != p:
                if not self.check(u, v):
                    return False
        return True

    def solve(self):
        self.dfs(0)
        if not self.check(0):
            return False
        return True


def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        u -= 1
        v -= 1
        g.add_edge(u, v)

    if not g.solve():
        print("NO")
    else:
        print("YES")
        ans = [0] * m
        for v in range(n):
            for u in g.adj[v]:
                if u > v:
                    ans[u] = 1
        print("".join(map(str, ans)))


if __name__ == '__main__':
    main()