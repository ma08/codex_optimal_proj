

import sys
import itertools

def input():
    return sys.stdin.readline().strip()

# N: the number of vertices
# M: the number of edges
N, M = map(int, input().split())

# a_i b_i: the i-th edge
edges = []
for i in range(M):
    a_i, b_i = map(int, input().split())
    edges.append((a_i, b_i))

#print(N, M, edges)

# initialize the adjacency matrix
adj_mat = [[0 for i in range(N)] for j in range(N)]

# update the adjacency matrix
for edge in edges:
    a_i, b_i = edge
    adj_mat[a_i-1][b_i-1] = 1
    adj_mat[b_i-1][a_i-1] = 1

#print(adj_mat)

# the number of paths
count = 0

# count the number of paths
for path in itertools.permutations(range(1, N)):
    #print(path)
    path = [0] + list(path)
    i = 0
    j = 1
    while True:
        if adj_mat[path[i]][path[j]]:
            i = j
            j += 1
            if j == N:
                count += 1
                break
        else:
            break

#print(count)
print(count)