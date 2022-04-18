import sys
from collections import defaultdict

def main():
    n, m, s = map(int, sys.stdin.readline().split())
    edges = defaultdict(list)
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
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
