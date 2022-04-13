import sys

class DSU:
    def __init__(self):
        self.parent = range(10**6)
        self.ranks = [0]*10**6
        self.size = [1]*10**6

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        elif self.ranks[xr] < self.ranks[yr]:
            self.parent[xr] = yr
            self.size[yr] += self.size[xr]
        elif self.ranks[xr] > self.ranks[yr]:
            self.parent[yr] = xr
            self.size[xr] += self.size[yr]
        else:
            self.parent[yr] = xr
            self.ranks[xr] += 1
            self.size[xr] += self.size[yr]

dsu = DSU()

for i in range(input()):
    line = sys.stdin.readline().split()
    if line[0] == "s":
        print(dsu.size[dsu.find(int(line[1]))])
    else:
        dsu.union(int(line[1]), int(line[2]))
