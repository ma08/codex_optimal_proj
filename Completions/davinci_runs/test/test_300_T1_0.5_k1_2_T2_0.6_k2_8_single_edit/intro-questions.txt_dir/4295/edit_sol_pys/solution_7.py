N, K = map(int, input().split())
ans = 0


for i in range(1, N+1):
    if N/i <= K:
        ans = i
        break

if N % K == 0:
    print(0)
else:
    print(min(N % K, K - (N % K)))
