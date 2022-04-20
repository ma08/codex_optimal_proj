#!/usr/bin/env python3

import sys
from collections import defaultdict

def main():
    n, m, s = sys.stdin.readline().split()
    n, m, s = int(n), int(m), int(s) - 1
    edges = defaultdict(list)
    for i in range(m):
        u, v = sys.stdin.readline().split()
        u, v = int(u) - 1, int(v) - 1
        edges[u].append(v)
    visited = set()
    stack = [s]
    while stack:
        node = stack.pop()
        visited.add(node)
        for edge in edges[node]:
            if edge not in visited:
                q.append(edge)
    print(n - len(visited))

main()
