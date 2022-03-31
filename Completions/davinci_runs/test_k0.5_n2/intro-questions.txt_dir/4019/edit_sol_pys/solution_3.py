
n, m, D = map(int, input().split())
edges = []
for _ in range(m):
    edges.append([int(x) for x in input().split()])

# Sort edges by the lowest vertex first
edges.sort(key=lambda x: x[0])

# Find the vertex with the lowest degree
# If it is the first vertex, we are done
# Otherwise, print the edge to the first vertex
# and remove it from the list of edges
degrees = [0] * (n + 1)
for edge in edges:
    degrees[edge[0]] += 1
    degrees[edge[1]] += 1
min_degree = min(degrees[1:])
if min_degree == D:
    print("YES")
    for edge in edges:
        print(edge[0], edge[1])
else:
    print("YES")
    edge_to_add = None
    for edge in edges:
        if degrees[edge[0]] == min_degree:
            edge_to_add = [edge[0], edge[1]]
            break
    edges.remove(edge_to_add)
    print(edge_to_add[0], edge_to_add[1])
    degrees[edge_to_add[0]] -= 1
    degrees[edge_to_add[1]] -= 1

# Add the remaining edges to the tree
for edge in edges:
    print(edge[0], edge[1])
