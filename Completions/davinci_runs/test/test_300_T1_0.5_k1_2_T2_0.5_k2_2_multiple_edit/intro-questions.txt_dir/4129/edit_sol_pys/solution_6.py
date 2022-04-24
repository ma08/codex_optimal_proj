


import sys
import os

def main():
    n, m, s = map(int, sys.stdin.readline().strip().split())
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
    stack = [s]
    while stack:
        u = stack.pop()
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)

    # Counting
    res = 0
    for i in range(1, n+1):
        if i == s:
            continue
        if not visited[i]:
            res += 1

    print(res)


if __name__ == '__main__':
    main()
