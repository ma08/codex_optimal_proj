

import sys
import math

def solve(k, dna):
    n = len(dna)  # number of dna
    edge = [[0 for i in range(n)] for j in range(n)]  # edge weight
    for i in range(n):  # calculate edge weight
        for j in range(i+1, n):  # only calculate upper triangle
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    edge[i][j] += 1
                    edge[j][i] += 1
    mst = [[math.inf for i in range(n)] for j in range(n)]  # minimum spanning tree
    used = [False for i in range(n)]  # if i-th dna is used
    mst[0][0] = 0  # first row is 0
    ans = 0  # answer
    for i in range(n):  # each row
        v = -1
        for j in range(n):  # find minimum edge weight
            if not used[j] and (v == -1 or mst[j][i] < mst[v][i]):
                v = j
        used[v] = True  # current dna is used
        ans += mst[v][i]  # add edge weight
        for j in range(n):  # update minimum edge weight
            if mst[j][i] > edge[v][j]:
                mst[j][i] = edge[v][j]
    print(ans)  # print answer
    for i in range(n):  # print minimum spanning tree
        for j in range(i+1, n):
            if mst[i][j] != math.inf:  # if edge weight is not infinite
                print(i, j)  # print edge

def main():
    line = sys.stdin.readline()  # input n and k
    n, k = [int(x) for x in line.split()]  # parse n and k
    dna = [sys.stdin.readline().strip() for i in range(n)]  # input dna
    solve(k, dna)

if __name__ == "__main__":
    main()
