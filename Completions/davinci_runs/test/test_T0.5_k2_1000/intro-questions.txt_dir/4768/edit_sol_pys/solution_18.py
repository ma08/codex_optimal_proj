

import sys
import math

def solve(k, dna):
    n = len(dna)
    edge = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    edge[i][j] += 1
                    edge[j][i] += 1
    mst = [[math.inf for i in range(n)] for j in range(n)] # minimum spanning tree
    used = [False for i in range(n)]
    mst[0][0] = 0
    ans = 0
    for i in range(n):
        v = -1
        for j in range(n):
            if not used[j] and (v == -1 or mst[j][i] < mst[v][i]): # v is the next vertex to be added
                v = j
        used[v] = True
        ans += mst[v][i]
        for j in range(n):
            if mst[j][i] > edge[v][j]:
                mst[j][i] = edge[v][j]
    print(ans)
    for i in range(n):
        for j in range(n):
            if mst[i][j] != math.inf:
                print(i, j)

def main():
    line = sys.stdin.readline()
    n, k = [int(x) for x in line.split()]
    dna = [sys.stdin.readline().strip() for i in range(n)]
    solve(k, dna)

if __name__ == "__main__":
    main()
