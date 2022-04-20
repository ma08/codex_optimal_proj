


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    offers = []
    for _ in range(m):
        x, y, w = map(int, input().split())
        offers.append((x, y, w))
    offers.sort(key=lambda x: x[2])
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i+1, j+1, a[i]+a[j]))
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    ans = 0
    for i in range(m):
        x, y, w = offers[i]
        if not uf.is_connected(x-1, y-1):
            uf.union(x-1, y-1)
            ans += w
    for i in range(n*(n-1)//2):
        x, y, w = edges[i]
        if not uf.is_connected(x-1, y-1):
            uf.union(x-1, y-1)
            ans += w
    print(ans)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.size[px] += self.size[py]
        self.parent[py] = px

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


if __name__ == "__main__":
    main()