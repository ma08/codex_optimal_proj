
N,M,X = list(map(int,input().split()))

A = [list(map(int,input().split())) for _ in range(N)]
C = list(map(int,input().split()))

inf = 10**18
ans = inf
for i in range(2**N):
    cost = 0
    algo = [0]*M
    for j in range(N):
        if (i>>j)&1:
            cost += C[j]
            for k in range(M):
                algo[k]+=A[j][k]
    if all(x>=X for x in algo):
        ans = min(ans,cost)

if ans==inf:
    print(-1)
else:
    print(ans)