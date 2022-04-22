"""
This is a template file that can be used for the solution of
the problem in the file
"""

import sys
import os

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    roads = []
    for i in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        roads.append((u, v))

    # Graph
    graph = [[] for i in range(n+1)]
    for (u, v) in roads:
        graph[u].append(v)

    # DFS
    visited = [False for i in range(n+1)]
    stack = []
    res = 0
    while stack:
        u = stack.pop()
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)

                res += 1

    print(res)


if __name__ == '__main__':
    main()
