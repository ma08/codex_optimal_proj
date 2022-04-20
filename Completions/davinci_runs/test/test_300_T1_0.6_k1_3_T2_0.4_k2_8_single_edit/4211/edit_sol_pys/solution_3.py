

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for i in range(1, N):
    ans += min(K, A[i] + A[i-1])
    A[i] = max(0, A[i] + A[i-1] - K)

print(ans)
