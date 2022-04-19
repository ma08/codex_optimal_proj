

import sys
import os

def main():
    n, m, s = map(int, sys.stdin.readline().strip().split())
    print(n, m, s)
    roads = []
    for i in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        print(u, v)
        roads.append((u, v))

    # Graph
    graph = [[] for i in range(n)]
    for (u, v) in roads:
        graph[u].append(v)
    print(graph)

    # DFS
    visited = [False for i in range(n)]
    stack = [s]
    while stack:
        u = stack.pop()
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)

    # Count
    res = 0
    for i in range(n):
        if i == s:
            continue
        if not visited[i]:
            res += 1

    print(res)


if __name__ == '__main__':
    main()
