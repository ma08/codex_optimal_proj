

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
    mst = [[math.inf for i in range(n)] for j in range(n+1)]
    used = [False for i in range(n)]
    mst[0][0] = 0
    ans = 0
    for i in range(n+1):
        v = -1
        for j in range(n):
            if not used[j] and (v == -1 or mst[i][j] < mst[i][v]):
                v = j
        used[v] = True
        ans += mst[i][v]
        for j in range(n):
            if mst[i+1][j] > edge[v][j]:
                mst[i+1][j] = edge[v][j]
    print(ans)
    for i in range(n):
        for j in range(n):
            if mst[n][i] != math.inf:
                print(i, j)

def main():
    line = sys.stdin.readline()
    n, k = [int(x) for x in line.split()]
    dna = [sys.stdin.readline().strip() for i in range(n)]
    solve(k, dna)

if __name__ == "__main__":
    main()
