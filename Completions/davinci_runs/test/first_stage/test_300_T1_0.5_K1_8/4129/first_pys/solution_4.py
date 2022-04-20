

import sys

def dfs(graph, start, visited):
    if visited[start]: return
    visited[start] = 1
    for node in graph[start]:
        dfs(graph, node, visited)

def main():
    n, m, start = [int(x) for x in sys.stdin.readline().split()]
    graph = [[] for i in range(n)]
    visited = [0] * n
    for i in range(m):
        u, v = [int(x) for x in sys.stdin.readline().split()]
        graph[u - 1].append(v - 1)
    dfs(graph, start - 1, visited)
    print(visited.count(0) - 1)

if __name__ == '__main__':
    main()