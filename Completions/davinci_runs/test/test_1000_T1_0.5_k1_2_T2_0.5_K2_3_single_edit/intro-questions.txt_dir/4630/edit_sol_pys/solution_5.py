

# SOLUTION
# The idea is to use a union-find structure to keep track of the cycles of the permutation.
# The cycle length is the number of days it takes for a book to return to its owner.
# We can use the union-find structure to quickly find the cycle length of a book.

# In addition to the union-find structure, we keep track of the current cycle length
# for each book. This allows us to quickly update the cycle length of a book when
# the book is given to another child.

# The time complexity is O(N log N) since we perform at most N union operations
# and each union operation takes O(log N) time due to path compression.

# The space complexity is O(N) since we store N elements in the union-find structure

class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N
        self.cycle = [1] * N

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
        N = int(input())
        p = list(map(int, input().split()))
        uf = UnionFind(N)
        for i in range(N):
            uf.union(i, p[i] - 1)
            print(uf.cycle[uf.find(i)], end=" ")
        print()

# I/O

if __name__ == "__main__":
    solve()
