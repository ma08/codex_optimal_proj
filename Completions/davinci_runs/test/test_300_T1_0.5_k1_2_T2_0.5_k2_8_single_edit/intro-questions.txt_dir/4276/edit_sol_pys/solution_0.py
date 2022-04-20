
N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
for i in range(1, N):
    if A[i] < A[i-1]:
        ans += A[i-1] - A[i]
        A[i] = A[i-1]
print(ans)
