#read input
n, q = map(int, input().split())
parents = [i for i in range(n)]
sizes = [1 for i in range(n)]

#find root of node
def find(node):
    if node == parents[node]:
        return node
    parents[node] = find(parents[node])
    return parents[node]

#union two nodes
def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)
    if node1 != node2:
        parents[node1] = node2
        sizes[node2] += sizes[node1]
        sizes[node1] = 0
