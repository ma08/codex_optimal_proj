

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + a[j-1])

print(dp[k][n])

# reconstruct answer
ans = []
i = k
j = n
while i > 0:
    if dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans.append(j)
        j -= 1
        i -= 1
ans.reverse()

for i in ans:
    print(i - ans[ans.index(i) - 1] if ans.index(i) > 0 else i, end=" ")