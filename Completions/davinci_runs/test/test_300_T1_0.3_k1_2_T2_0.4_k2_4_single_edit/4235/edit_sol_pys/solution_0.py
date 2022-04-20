
import sys
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def dfs(self, u, v):
        if u == v:
            return True
        for w in self.edges[u]:
            if w != v and self.dfs(w, v):
                return True
        return False

def main():
    n, m = map(int, sys.stdin.readline().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        g.add_edge(u, v)
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if u != v and not g.dfs(u, v):
                print("NO")
                return
    print("YES")
    for u in range(1, n + 1):
        for v in g.edges[u]:
            if v > u:
                print("0", end="")
            else:
                print("1", end="")
    print()

if __name__ == "__main__":
    main()
