

#union find - array

#find root of node - O(n)
def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]

#union two nodes - O(1)
def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)
    if node1 != node2:
        parents[node1] = node2

#read input
n, q = map(int, input().split())
parents = [i for i in range(n)]

#run queries
for i in range(q):
    query = input().split()
    if query[0] == 't':
        union(int(query[1])-1, int(query[2])-1)
    else:
        print(sizes[find(int(query[1])-1)])
