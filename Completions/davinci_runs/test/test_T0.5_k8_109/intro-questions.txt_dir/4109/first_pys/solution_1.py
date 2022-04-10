

N,M,X = map(int,input().split())

A = []
C = []

for i in range(N):
    A.append(list(map(int,input().split())))
    C.append(A[-1].pop(0))

def dfs(i,sum,algo):
    global ans
    if sum >= ans:
        return
    if algo >= X:
        ans = min(ans,sum)
        return
    if i == N:
        return
    dfs(i+1,sum,algo)
    dfs(i+1,sum+C[i],algo+A[i][0])

ans = 10**10
dfs(0,0,0)
if ans == 10**10:
    print(-1)
else:
    print(ans)