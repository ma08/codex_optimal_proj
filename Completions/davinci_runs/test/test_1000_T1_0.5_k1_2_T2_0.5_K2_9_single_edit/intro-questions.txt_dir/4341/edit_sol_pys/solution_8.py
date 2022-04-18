

def count_cycles(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            count += 1
    return count

def dfs(graph, node, visited):
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph, child, visited)
