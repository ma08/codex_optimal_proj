

def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    edges = []
    for i in range(m):
        x, y, w = [int(x) for x in input().split()]
        edges.append((x-1, y-1, w))
    edges.sort(key=lambda x: x[2])
    uf = UF(n)
    result = 0
    for edge in edges:
        if uf.find(edge[0]) != uf.find(edge[1]):
            result += edge[2]
            uf.union(edge[0], edge[1])
    if uf.count != 1:
        result += min(a)
    print(result)

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.count = n

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        self.count -= 1

if __name__ == "__main__":
    main()