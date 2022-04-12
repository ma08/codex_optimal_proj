import sys

def dfs(graph, vertex, visited):
    visited.add(vertex)
    for child in graph[vertex]:
        if child not in visited:
            dfs(graph, child, visited)

def count_cycles(graph):
    visited = set()
    cycles = 0

    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited)
            cycles += 1
    return cycles

def main():
    n, m = map(int, sys.stdin.readline().split())

    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(count_cycles(graph))

if __name__ == '__main__':
    main()
