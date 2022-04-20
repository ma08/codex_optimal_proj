
import sys

def get_input(file=None):
    if file is None:
        fh = sys.stdin
    else:
        fh = open(file)

    def read_int():
        return int(fh.readline())

    def read_ints():
        return [int(x) for x in fh.readline().split()]

    n, k = read_ints()
    assert 1 <= n <= 200000
    assert 0 <= k <= n-1

    return n, k

def get_graph(n, file=None):
    if file is None:
        fh = sys.stdin
    else:
        fh = open(file)

    def read_int():
        return int(fh.readline())

    def read_ints():
        return [int(x) for x in fh.readline().split()]

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = read_ints()
        assert 1 <= x <= n
        assert 1 <= y <= n
        graph[x].append(y)
        graph[y].append(x)

    return graph

def get_roof(graph):
    n = len(graph)-1
    visited = set()
    queue = [1]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        queue.extend(graph[node])

    assert len(visited) == n

    return visited

def get_children(graph, node):
    children = set()
    for child in graph[node]:
        if child != node:
            children.add(child)
    return children

def get_distances(graph, node):
    distances = {node: 0}
    queue = [node]
    while queue:
        node = queue.pop(0)
        distance = distances[node]
        for child in graph[node]:
            if child not in distances:
                distances[child] = distance + 1
                queue.append(child)

    return distances

def get_leaf(graph, node):
    for child in graph[node]:
        if child != node:
            return child
    raise ValueError('node is not a root')

def get_leaves(graph, node):
    leaves = set()
    queue = [node]
    while queue:
        node = queue.pop(0)
        if len(graph[node]) == 1:
            leaves.add(node)
        else:
            for child in graph[node]:
                if child != node:
                    queue.append(child)
    return leaves

def get_root(graph, node):
    root = node
    while graph[root][0] != root:
        root = graph[root][0]
    return root

def get_strategy(graph, n, k):
    roof = get_roof(graph)
    if len(roof) == 1:
        return 1

    distances = get_distances(graph, 1)
    root = max(distances, key=lambda x: distances[x])
    root_distance = distances[root]

    leaves = get_leaves(graph, root)
    assert len(leaves) >= 2

    # print(root, leaves)

    if len(leaves) == 2:
        if root_distance == 1:
            return 1
        else:
            return 2

    if root_distance == 1:
        if len(leaves) <= k+1:
            return 1
        else:
            return 2

    if len(leaves) <= k:
        return 2

    return 3

def get_solution(graph, n, k):
    strategy = get_strategy(graph, n, k)
    if strategy == 1:
        return [1]*(n-1)
    elif strategy == 2:
        companies = [1]*(n-1)
        distances = get_distances(graph, 1)
        root = max(distances, key=lambda x: distances[x])
        leaves = get_leaves(graph, root)
        assert len(leaves) >= 2

        for leaf in leaves:
            node = leaf
            while node != root:
                companies[node-1] = 2
                node = graph[node][0]
        return companies
    else:
        companies = [1]*(n-1)
        distances = get_distances(graph, 1)
        root = max(distances, key=lambda x: distances[x])
        leaves = get_leaves(graph, root)
        assert len(leaves) >= 3

        for leaf in leaves:
            node = leaf
            while node != root:
                companies[node-1] = 2
                node = graph[node][0]
        return companies

def main():
    n, k = get_input()
    graph = get_graph(n)
    solution = get_solution(graph, n, k)
    print(max(solution))
    print(*solution)

if __name__ == '__main__':
    main()