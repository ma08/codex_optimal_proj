

from collections import defaultdict

def add_edge(u, v):
    graph[u].append(v)


def dfs(node, parent):
    for child in graph[node]:
        if child != parent:
            dfs(child, node)


def solve():
    dfs(1, 0)


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    graph = defaultdict(list)
    for i in range(m):
        u, v = [int(x) for x in input().split()]
        add_edge(u, v)
        add_edge(v, u)
    solve()
