

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def connected_components(graph):
    seen = set()
    for vertex in graph:
        if vertex not in seen:
            component = bfs(graph, vertex)
            yield component
            seen.update(component)


def main():
    graph = {
        "a": set(["b", "c"]),
        "b": set(["a", "d"]),
        "c": set(["a", "d"]),
        "d": set(["e"]),
        "e": set(["a"])
    }

    print(dfs(graph, "a"))
    print(bfs(graph, "a"))

    print(list(connected_components(graph)))


if __name__ == '__main__':
    main()
