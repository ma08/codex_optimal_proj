

import sys
n = int(sys.stdin.readline())

# read edges
edges = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

# get the degree of each node
degree = [0] * (n+1)
for i in range(1, n+1):
    degree[i] = len(edges[i])

# get the node with maximum degree
max_degree = max(degree)
max_degree_node = degree.index(max_degree)

# get the second node with maximum degree
# and remove the edge between the two nodes
second_max_degree = 0
second_max_degree_node = 0
for i in edges[max_degree_node]:
    if degree[i] > second_max_degree:
        second_max_degree = degree[i]
        second_max_degree_node = i
edges[max_degree_node].remove(second_max_degree_node)
edges[second_max_degree_node].remove(max_degree_node)

# get the third node with maximum degree
# and remove the edge between the two nodes
third_max_degree = 0
third_max_degree_node = 0
for i in edges[max_degree_node]:
    if degree[i] > third_max_degree:
        third_max_degree = degree[i]
        third_max_degree_node = i
edges[max_degree_node].remove(third_max_degree_node)
edges[third_max_degree_node].remove(max_degree_node)

print(max_degree + second_max_degree + third_max_degree)
print(max_degree_node, second_max_degree_node, third_max_degree_node)