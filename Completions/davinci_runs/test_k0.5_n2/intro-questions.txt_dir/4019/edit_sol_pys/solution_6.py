

import sys
import math
from collections import defaultdict

# n = num vertices
# m = num edges
# d = degree of vertex 1
n, m, d = map(int, sys.stdin.readline().split())

# create adjacency list
adj_list = defaultdict(list)
for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

# create list of degrees
degrees = [0] * n
for v in adj_list:
    degrees[v - 1] = len(adj_list[v])

# check if there exists a tree with degree d
# if not, print NO
if d > max(degrees):
    print("NO")
    exit()

# create list of vertices to visit and visited list
# initialise visited list
to_visit = [1]
visited = [False] * n
visited[0] = True

# create list of edges in tree
tree_edges = []

# while there are still vertices to visit
while to_visit:
    # visit next vertex
    v = to_visit.pop()
    for n in adj_list[v]:
        # if vertex is unvisited
        if not visited[n - 1]:
            # add edge to tree
            tree_edges.append([v, n])
            # add vertex to visit
            to_visit.append(n)
            # mark as visited
            visited[n - 1] = True

# print YES
print("YES")

# if degree of vertex 1 is not d
if degrees[0] != d:
    # find unvisited vertex
    for v in range(1, n):
        if not visited[v - 1]:
            # add edge from vertex 1 to unvisited vertex
            tree_edges.append([1, v + 1])
            # print edge
            print(1, v + 1)
            # mark vertex as visited
            visited[v - 1] = True
            # break
            break

# print tree edges
for edge in tree_edges:
    print(edge[0], edge[1])
