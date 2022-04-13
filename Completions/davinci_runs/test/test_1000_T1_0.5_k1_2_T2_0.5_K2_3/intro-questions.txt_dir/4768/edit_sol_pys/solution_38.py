from math import sqrt
from collections import defaultdict


def parse_data():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    return n, edges

    # Construct a table of distances between each pair of strings
    distances = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    distances[i][j] += 1

    # Compute the minimal spanning tree
    tree = []
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, distances[i][j]))
    edges = sorted(edges, key=lambda x: x[2])

    # Use Kruskal's algorithm to find the minimal spanning tree
    def find(parent, child):
        while parent[child] != child:
            child = parent[child]
        return child

    parent = list(range(n))
    for i, j, dist in edges:
        root_i, root_j = find(parent, i), find(parent, j)
        if root_i != root_j:
            tree.append((i, j, dist))
            parent[root_i] = root_j

    # Print the result
    print(sum(dist for _, _, dist in tree))
    for i, j, _ in tree:
        print(i, j)


if __name__ == '__main__':
    main()
