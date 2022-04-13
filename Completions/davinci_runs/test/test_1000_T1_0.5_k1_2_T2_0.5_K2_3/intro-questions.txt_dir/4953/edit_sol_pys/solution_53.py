
# This is a graph problem, I assume.
# Build a directed graph where each node is a person, and each edge is a language.
# The problem can be solved by finding the strongly connected components and then
# finding the smallest set of nodes to remove.
# This is a variant of the problem: https://www.hackerrank.com/challenges/strongly-connected

from collections import defaultdict

def read_input():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n):
        line = input().split()
        node = line[0]
        graph[node] = line[2:]
    return graph

def dfs(graph, start, visited, postorder, postorder_index):
    """
    Depth-first search.
    """
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited, postorder, postorder_index)
    postorder[start] = postorder_index[0]
    postorder_index[0] -= 1

def reverse_graph(graph):
    """
    Reverses the graph by switching the nodes with the edges.
    """
    reversed_graph = defaultdict(list)
    for node in graph:
        for edge in graph[node]:
            reversed_graph[edge].append(node)
    return reversed_graph

def get_strongly_connected_components(graph):
    """
    Returns a list of strongly connected components.
    """
    visited = set()
    postorder = {}
    postorder_index = [len(graph)]
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, postorder, postorder_index)

    graph = reverse_graph(graph)
    visited = set()
    components = []
    for node in sorted(postorder, key=postorder.get):
        if node not in visited:
            component = []
            dfs(graph, node, visited, {}, component)
            components.append(component)
    return components

def get_smallest_set(graph):
    """
    Returns the smallest set of nodes to remove from the graph.
    """
    components = get_strongly_connected_components(graph)
    min_size = len(graph)
    for component in components:
        min_size = min(min_size, len(graph) - len(component))
    return min_size

def main():
    graph = read_input()
    print(get_smallest_set(graph))

if __name__ == "__main__":
    main()
