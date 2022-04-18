import sys
from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start, visited):
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(graph, next, visited)

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        add_edge(graph, a, b)
    visited = [False] * (N+1)
    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    print(count)

if __name__ == "__main__":
    main()
