from collections import defaultdict
import sys


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.visited = defaultdict(bool)
        self.start = None
        self.end = None

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def dfs(self, src):
        self.visited[src] = True

        if src == self.end:
            return 0

        min_dist = sys.maxsize
        for v, w in sorted(self.adj[src], key=lambda x: x[1]):
            if not self.visited[v]:
                dist = self.dfs(v) + w
                if dist < min_dist:
                    min_dist = dist

        return min_dist

    def get_min_dist(self, start, end):
        self.start = start
        self.end = end
        return self.dfs(start)


def main():
    g = Graph()
    n, m = [int(x) for x in input().split()]
    for _ in range(m):
        u, v, w = [int(x) for x in input().split()]
        g.add_edge(u, v, w)

    q = int(input())
    for _ in range(q):
        u, v = [int(x) for x in input().split()]
        print(g.get_min_dist(u, v))


if __name__ == '__main__':
    main()
