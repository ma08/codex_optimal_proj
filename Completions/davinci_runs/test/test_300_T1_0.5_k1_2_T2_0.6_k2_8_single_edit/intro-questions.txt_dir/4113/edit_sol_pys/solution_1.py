N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
for i in range(N):
    tmp = 0
    for j in range(i, N):
        tmp += A[j]
        ans += tmp
print(ans)

