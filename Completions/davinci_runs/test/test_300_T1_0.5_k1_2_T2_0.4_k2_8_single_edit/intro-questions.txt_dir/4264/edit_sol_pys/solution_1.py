

N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = []
for i in range(M):
    B.append(int(input()))

for i in range(N):
    ans = 0
    for j in range(M):
        ans += A[i][j] * B[j]
    print(ans)
