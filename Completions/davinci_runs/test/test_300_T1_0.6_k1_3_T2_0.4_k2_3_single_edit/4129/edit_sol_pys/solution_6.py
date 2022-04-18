import sys
from collections import deque



class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def bfs(self, s):
        visited = [False] * self.n
        q = deque([s])
        while q:
            node = q.popleft()
            visited[node] = True
            for edge in self.adj[node]:
                if not visited[edge]:
                    q.append(edge)
        return visited


def main():
    n, m, s = sys.stdin.readline().split()
    n, m, s = int(n), int(m), int(s)
    edges = defaultdict(list)
    for i in range(m):
        u, v = sys.stdin.readline().split()
        u, v = int(u), int(v)
        edges[u].append(v)
    visited = set()
    q = [s]
    while q:
        node = q.pop()
        visited.add(node)
        for edge in edges[node]:
            if edge not in visited:
                q.append(edge)
    print(n - len(visited))

main()
