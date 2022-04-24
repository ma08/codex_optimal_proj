import sys
sys.setrecursionlimit(10**7)


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    while queue:
        current = queue.pop(0)
        if not visited[current]:
            visited[current] = True
            queue.extend(graph[current])
    return visited


def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack.extend(graph[current])
    return visited


def dfs_recursive(graph, start, visited):
    visited[start] = True
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs_recursive(graph, next_node, visited)


def dfs_recursive_all(graph):
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            dfs_recursive(graph, i, visited)


def topological_sort(graph):
    stack = []
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            topological_sort_recursive(graph, i, visited, stack)
    return stack[::-1]


def topological_sort_recursive(graph, start, visited, stack):
    visited[start] = True
    for next_node in graph[start]:
        if not visited[next_node]:
            topological_sort_recursive(graph, next_node, visited, stack)
    stack.append(start)


def main():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for i in range(e):
        s, t = map(int, input().split())
        graph[s].append(t)
    print(topological_sort(graph))


if __name__ == '__main__':
    main()
