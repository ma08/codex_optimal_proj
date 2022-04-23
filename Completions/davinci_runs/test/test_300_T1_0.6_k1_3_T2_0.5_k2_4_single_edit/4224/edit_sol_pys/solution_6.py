

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    if a[i] % 2 == 0:
        count += 1

print(count)
