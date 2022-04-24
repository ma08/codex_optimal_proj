

import sys
import numpy as np
from collections import defaultdict

def dfs(s, visited, graph, d):
    visited[s] = True
    if s in graph:
        for i in graph[s]:
            if not visited[i]:
                dfs(i, visited, graph, d + 1)
    else:
        if d > max_d:
            max_d = d
    global max_d
    max_d = 0

def main():
    n, m, s = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)

    visited = np.zeros(n + 1)
    dfs(s, visited, graph, 0)

    res = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited, graph, 0)
            res += 1
    print(res, max_d)

if __name__ == '__main__':
    main()
