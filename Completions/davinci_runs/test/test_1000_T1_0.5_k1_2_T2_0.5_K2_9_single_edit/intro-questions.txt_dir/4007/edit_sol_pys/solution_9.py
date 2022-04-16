'''
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6	155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc
'''

n = int(input())
f = [int(x) for x in input().split()[1:]]

# Find friends who don't know who to give gifts to
# and friends who don't know who gives them gifts
no_gift_to = []
no_gift_from = []
for i in range(n):
    if f[i] == 0:
        no_gift_to.append(i)
    else:
        if f[f[i] - 1] == 0:
            no_gift_from.append(f[i] - 1)

# Give gifts to friends who don't know who gives them gifts
for i in range(len(no_gift_to)):
    f[no_gift_from[i]] = no_gift_to[i] + 1

# Give gifts to friends who don't know who to give gifts to
for i in range(len(no_gift_to)):
    f[no_gift_to[i]] = no_gift_from[i] + 1

print(" ".join(str(x) for x in f))
