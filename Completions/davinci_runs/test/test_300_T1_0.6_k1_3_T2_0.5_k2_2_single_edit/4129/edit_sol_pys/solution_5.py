
import sys
from collections import defaultdict


def bfs(n, m, s):
    edges = defaultdict(set)
    for _ in range(m):
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
