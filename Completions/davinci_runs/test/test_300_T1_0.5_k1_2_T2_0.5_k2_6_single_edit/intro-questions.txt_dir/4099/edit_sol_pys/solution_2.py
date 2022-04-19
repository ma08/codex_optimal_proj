
N, K = map(int, input().split())
A = list(map(int, input().split())) + [0]

ans = 0
for i in range(N):
    if A[i] + A[i+1] < K:
        ans += K - (A[i] + A[i+1])
        A[i+1] += K - (A[i] + A[i+1])

print(ans)
print(*A[:-1])
