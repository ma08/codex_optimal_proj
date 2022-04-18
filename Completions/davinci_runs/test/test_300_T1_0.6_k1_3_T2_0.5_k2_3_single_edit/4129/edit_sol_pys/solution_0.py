
#!/usr/bin/python

import sys
import numpy as np
from collections import defaultdict

def dfs(s, visited, graph):
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(i, visited, graph)

def main():
    n, m, s = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[v].append(u)

    visited = np.zeros(n + 1)
    dfs(s, visited, graph)

    res = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph)
            res += 1
    print(res)

if __name__ == '__main__':
    main()
