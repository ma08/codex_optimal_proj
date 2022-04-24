<<<<<<< HEAD

import sys
from collections import defaultdict

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
=======
import sys
from collections import defaultdict

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
>>>>>>> c9e7e9c8d2f1ffa0f2a6c3e3b8e6e7a6b9cd9f0c
