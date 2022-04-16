
import sys

class DisjointSets:
    def __init__(self, n):
        self.sets = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, i):
        if self.sets[i] != i:
            self.sets[i] = self.find(self.sets[i])
        return self.sets[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            i, j = j, i
        self.sets[j] = i
        self.size[i] += self.size[j]

n, q = map(int, input().split())
disjoint_sets = DisjointSets(n)
for _ in range(q):
    query = input().split()
    if query[0] == 't':
        disjoint_sets.union(int(query[1]), int(query[2]))
    elif query[0] == 's':
        print(disjoint_sets.size[disjoint_sets.find(int(query[1]))])
