

# SOLUTION

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
