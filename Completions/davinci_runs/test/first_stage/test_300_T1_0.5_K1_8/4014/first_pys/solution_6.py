

from collections import defaultdict

class Graph(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, u, visited):
        stack = [u]
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                stack.extend(self.graph[u])
        return visited

    def is_cyclic(self):
        visited = set()

        for u in self.graph:
            if u not in visited:
                visited = self._dfs(u, visited)
        return len(visited) != self.n + self.m + 2


def main():
    n, m = map(int, input().split())
    g = Graph(n, m)
    for i in range(m):
        s, d, c = map(int, input().split())
        g.add_edge(0, i + 1)
        g.add_edge(i + 1, i + m + 1)
        g.add_edge(i + m + 1, n + m + 1)

        for j in range(s, d):
            g.add_edge(i + 1, j + m + 1)
    if g.is_cyclic():
        print(-1)
        return
    ans = [0] * n
    for i in range(n):
        for j in range(m):
            if i + m + 1 in g.graph[j + 1]:
                ans[i] = j + 1
    for i in range(m):
        if n + m + 1 in g.graph[i + m + 1]:
            ans[d - 1] = m + 1
    print(*ans)


if __name__ == '__main__':
    main()