
from collections import defaultdict
n, m = [int(i) for i in input().split()]  # n - number of stations, m - number of connections


def create_graph(edges):
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


def find_cycle(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_cycle(graph, node, end, path)
            if newpath:
                return newpath
    return None


def find_all_cycles(graph, start, path=[]):
    path = path + [start]
    if start not in graph:
        return None
    cycles = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_cycles(graph, node, path)
            for newpath in newpaths:
                cycles.append(newpath)
        elif len(path) > 2 and node == path[0]:
            cycles.append(path + [node])
    return cycles


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_path_length(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return len(path) - 1
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path_length(graph, node, end, path)
            if newpath:
                if not shortest or newpath < shortest:
                    shortest = newpath
    return shortest


if __name__ == '__main__':
    edges = []
    for i in range(m):
        edges.append(tuple(int(i) for i in input().split()))
    graph = create_graph(edges)
    if m == n - 1:
        print(m)
    elif m <= n:
        print(m + 1)
    else:
        print(n + (m - n + 1) // 2)
