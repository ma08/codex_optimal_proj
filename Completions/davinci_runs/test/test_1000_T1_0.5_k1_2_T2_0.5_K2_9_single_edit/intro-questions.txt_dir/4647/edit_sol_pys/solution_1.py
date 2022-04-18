
# import the required modules
from sys import stdin
from collections import deque
# read the input
input_lines = deque(stdin.read().splitlines())
# read the number of vertices
n = int(input_lines.popleft())
# read the colors of the vertices
colors = list(map(int, input_lines.popleft().split()))
# read the edges
edges = []
for _ in range(n - 1):
    u, v = map(int, input_lines.popleft().split())
    edges.append((u - 1, v - 1))
# initialize the adjacency list
adj_list = [[] for _ in range(n)]
for (u, v) in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
# initialize the parent array
parent = [-1 for _ in range(n)]
# initialize the white and black count arrays
white_count = [0 for _ in range(n)]
black_count = [0 for _ in range(n)]
# initialize the queue
queue = deque()
# start with the first vertex
queue.append(0)
# perform BFS
while len(queue) > 0:
    # get the next vertex
    u = queue.popleft()
    # set the count of the vertex
    white_count[u] = colors[u]
    black_count[u] = 1 - colors[u]
    # visit all the neighbors of the vertex
    for v in adj_list[u]:
        # skip the parent vertex
        if v == parent[u]:
            continue
        # set the parent of the neighbor
        parent[v] = u
        # add the neighbor to the queue
        queue.append(v)
# initialize the result array
result = [0 for _ in range(n)]
# start with the last vertex
queue.append(n - 1)
# perform BFS
while len(queue) > 0:
    # get the next vertex
    u = queue.popleft()
    # update the result of the vertex
    result[u] = max(white_count[u] - black_count[u], 0)
    # visit all the neighbors of the vertex
    for v in adj_list[u]:
        # skip the parent vertex
        if v == parent[u]:
            continue
        # update the white and black counts of the neighbor
        white_count[v] += white_count[u]
        black_count[v] += black_count[u]
        # add the neighbor to the queue
        queue.append(v)
# print the result
print(' '.join(map(str, result)))
