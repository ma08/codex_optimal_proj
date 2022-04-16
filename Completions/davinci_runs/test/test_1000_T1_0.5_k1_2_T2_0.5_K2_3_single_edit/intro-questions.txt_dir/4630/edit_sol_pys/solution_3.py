

# SOLUTION
# The idea is to use a union-find structure to keep track of the cycles of the permutation.
# The cycle length is the number of days it takes for a book to return to its owner.
# We can use the union-find structure to quickly find the cycle length of a book.

# In addition to the union-find structure, we keep track of the current cycle length
# for each book. This allows us to quickly update the cycle length of a book when
# the book is given to another child.

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
        self.cycle = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id, j_id = self.find(i), self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            i_id, j_id = j_id, i_id
        self.parent[i_id] = j_id
        self.size[j_id] += self.size[i_id]
        self.cycle[j_id] = self.cycle[i_id] + self.cycle[j_id]
        if self.rank[i_id] == self.rank[j_id]:
            self.rank[j_id] += 1


def solve():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        uf = UnionFind(n)
        for i in range(n):
            uf.union(i, p[i] - 1)
            print(uf.cycle[uf.find(i)], end=" ")
        print()

# I/O

if __name__ == "__main__":
    solve()
