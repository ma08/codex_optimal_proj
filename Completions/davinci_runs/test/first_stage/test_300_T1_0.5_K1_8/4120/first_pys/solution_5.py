

# Solution

import sys

# Build a graph from the input.
# The graph is represented as a dictionary where each key is a node and the associated value is a list of its neighbors.
n, m, k = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = {i: [] for i in range(1, n+1)}
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# Find the shortest paths from the capital to all other cities.
# The shortest paths are represented as a dictionary where each key is a city and the associated value is the length of the shortest path from the capital to the city.
distances = {i: -1 for i in range(1, n+1)}
distances[1] = 0
to_visit = [1]
while to_visit:
    current = to_visit.pop(0)
    for neighbor in graph[current]:
        if distances[neighbor] == -1:
            distances[neighbor] = distances[current] + 1
            to_visit.append(neighbor)

# Sort the edges by their length in increasing order.
# Each edge is represented as a tuple (city1, city2, length).
sorted_edges = sorted([(a, b, distances[a] + distances[b]) for a, b in edges], key=lambda x: x[2])

# Find the $k$ shortest paths from the capital to all other cities.
# Each path is represented as a dictionary where each key is a city and the associated value is the length of the path from the capital to the city.
# The paths are stored in a list of dictionaries.
paths = [{1: 0}]
for _ in range(k-1):
    # Add the shortest edge that connects the current path with another city.
    for edge in sorted_edges:
        if edge[0] in paths[-1] and edge[1] not in paths[-1]:
            paths[-1][edge[1]] = edge[2]
            break
        elif edge[1] in paths[-1] and edge[0] not in paths[-1]:
            paths[-1][edge[0]] = edge[2]
            break
    # If no edge can be added, then there are no more paths.
    else:
        break
    paths.append({1: 0})

# Output the paths.
print(len(paths))
for path in paths:
    print(''.join('1' if (a, b) in edges and b in path else '0' for a, b in edges))