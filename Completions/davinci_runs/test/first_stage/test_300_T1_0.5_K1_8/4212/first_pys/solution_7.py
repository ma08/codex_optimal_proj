

#import sys
#sys.setrecursionlimit(10**9)

n, m, q = [int(i) for i in input().split()]

a = [[0 for i in range(m)] for j in range(n+1)]

for i in range(1, n+1):
    a[i][0] = 1

for i in range(q):
    ai, bi, ci, di = [int(i) for i in input().split()]
    a[ai][ci] += di

for i in range(1, n+1):
    for j in range(1, m):
        a[i][j] += a[i][j-1]

for i in range(1, n+1):
    for j in range(1, m):
        a[i][j] += a[i-1][j]

print(a[n][m-1])