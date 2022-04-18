

N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]

# print(A)

ans = 0
for i in range(N):
    if M > A[i]:
        ans += M // A[i]
        M -= A[i] * (M // A[i])

print(ans)
