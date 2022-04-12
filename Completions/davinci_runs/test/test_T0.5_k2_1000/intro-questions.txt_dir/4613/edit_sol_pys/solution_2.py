
#------Solution------
import sys

def input():
    return sys.stdin.readline().strip()

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
    
    # find the root of the tree
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    # unite the tree
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    # check whether x and y are in the same trees
    def same(self, x, y):
        return self.find(x) == self.find(y)

ans = 0
u = UnionFind(N)
for a, b in edges:
    if not u.same(a, b):
        u.unite(a, b)
        ans += 1
print(M - ans)
