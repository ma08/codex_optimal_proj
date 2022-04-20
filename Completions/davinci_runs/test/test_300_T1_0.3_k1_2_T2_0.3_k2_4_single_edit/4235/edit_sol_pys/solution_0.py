
import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def bfs(self, u):
        q = deque()
        q.append(u)
        visited = [False] * (self.n + 1)
        visited[u] = True
        while q:
            u = q.popleft()
            for v in self.edges[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True
        return all(visited)

def main():
    n, m = map(int, sys.stdin.readline().split())
    g = Graph(n, m)
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
