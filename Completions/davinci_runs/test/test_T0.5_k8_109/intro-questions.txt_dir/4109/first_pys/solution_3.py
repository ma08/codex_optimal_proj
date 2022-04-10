

import sys
input = sys.stdin.readline

#input
N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = [int(input()) for _ in range(N)]

#solve
INF = 10**9
ans = INF
for i in range(2**N):
    cost = 0
    lis = [0]*M
    for j in range(N):
        if (i >> j) & 1:
            cost += C[j]
            for k in range(M):
                lis[k] += A[j][k]
    if all(x >= X for x in lis):
        ans = min(ans, cost)

if ans == INF:
    print(-1)
else:
    print(ans)