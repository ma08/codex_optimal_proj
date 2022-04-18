

# 全探索
N, M, X = map(int, input().split())
A = []
C = []
for _ in range(N):
    c, *a = map(int, input().split())
    A.append(a)
    C.append(c)

ans = 10**10
for i in range(1 << N):
    cost = 0
    level = [0] * M
    for j in range(N):
        if i & (1 << j):
            cost += C[j]
            for k in range(M):
                level[k] = max(level[k], A[j][k])
    if all(x >= X for x in level):
        ans = min(ans, cost)

if ans == 10**10:
    print(-1)
else:
    print(ans)
