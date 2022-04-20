

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]

dp = [[[float("inf") for _ in range(sum(l) + 1)] for _ in range(B + 1)] for _ in range(A + 1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(A + 1):
        for k in range(B + 1):
            for m in range(sum(l) + 1):
                if dp[j][k][m] == float("inf"):
                    continue
                if j + l[i] <= A:
                    dp[j + l[i]][k][m] = min(dp[j + l[i]][k][m], dp[j][k][m] + 1)
                if k + l[i] <= B:
                    dp[j][k + l[i]][m] = min(dp[j][k + l[i]][m], dp[j][k][m] + 1)
                if m + l[i] <= sum(l):
                    dp[j][k][m + l[i]] = min(dp[j][k][m + l[i]], dp[j][k][m] + 1)
                if j + l[i] <= A and k + l[i] <= B:
                    dp[j + l[i]][k + l[i]][m] = min(dp[j + l[i]][k + l[i]][m], dp[j][k][m] + 10)
                if j + l[i] <= A and m + l[i] <= sum(l):
                    dp[j + l[i]][k][m + l[i]] = min(dp[j + l[i]][k][m + l[i]], dp[j][k][m] + 10)
                if k + l[i] <= B and m + l[i] <= sum(l):
                    dp[j][k + l[i]][m + l[i]] = min(dp[j][k + l[i]][m + l[i]], dp[j][k][m] + 10)

ans = float("inf")
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(sum(l) + 1):
            if i == A and j == B and k == C:
                ans = min(ans, dp[i][j][k])

print(ans)