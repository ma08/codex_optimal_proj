

#---------------------------------------------------------------------------------

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
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)

    visited = np.zeros(n + 1, dtype=bool)
    dfs(s, visited, graph)

    res = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited, graph)
            res += 1
    print(res)

if __name__ == '__main__':
    main()
