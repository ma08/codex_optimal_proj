

# n, m, d = 4, 5, 1
# edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

n, m, d = 4, 5, 3
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

# n, m, d = 4, 4, 3
# edges = [[1, 2], [1, 4], [2, 3], [3, 4]]

# n, m, d = map(int, input().split())
# edges = [[int(x) for x in input().split()] for _ in range(m)]

def find_spanning_tree(n, m, d, edges):
    if m < n - 1:
        return "NO"
    if d > n - 1:
        return "NO"
    if m == n - 1:
        if d == n - 1:
            return "YES"
        else:
            return "NO"

    # Build adjacency list
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[0] - 1].append(edge[1] - 1)
        adj_list[edge[1] - 1].append(edge[0] - 1)

    # Find a spanning tree
    visited = set()
    queue = [0]
    tree = []
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                tree.append([node + 1, neighbor + 1])

    # Check if the spanning tree has the right degree
    if len(tree) != n - 1:
        return "NO"
    if len(adj_list[0]) == d:
        return "YES\n" + "\n".join([str(edge[0]) + " " + str(edge[1]) for edge in tree])
    else:
        return "NO"

print(find_spanning_tree(n, m, d, edges))