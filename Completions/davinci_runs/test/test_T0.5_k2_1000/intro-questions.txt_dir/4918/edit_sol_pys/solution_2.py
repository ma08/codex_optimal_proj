

#union-find (with path compression)

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]

    #find the root of a node
    def find(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    #union two nodes together
    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 != node2:
            self.parents[node1] = node2
            self.sizes[node2] += self.sizes[node1]
            self.sizes[node1] = 0

    #return the size of a node
    def size(self, node):
        return self.sizes[self.find(node)]

#read input
n, q = map(int, input().split())
uf = UnionFind(n)

#run queries
for i in range(q):
    query = input().split()
    if query[0] == 'u':
        uf.union(int(query[1])-1, int(query[2])-1)
    else:
        print(uf.size(int(query[1])-1))
