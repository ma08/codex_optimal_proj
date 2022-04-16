
import sys

def dfs(graph, node, visited):
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph, child, visited)

def count_components(graph):
    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            components += 1
    return components

def main():
    n, m = map(int, sys.stdin.readline().split())

    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)

    print(count_components(graph))

if __name__ == '__main__':
    main()
