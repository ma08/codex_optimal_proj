

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if i == j == 0:
            continue
        if i == 0:
            ans += A[i][j]
        elif j == 0:
            ans += A[i][j]
        else:
            ans += min(A[i][0], A[0][j])

print(ans)
