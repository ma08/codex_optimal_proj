
n = int(input())
a = list(map(int, input().split()))

# dp[i] = number of problems in the longest contest ending at problem i
dp = [0] * n

# dp[i] = max(dp[j] + 1) for j < i and a[j] * 2 >= a[i]
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] * 2 >= a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))