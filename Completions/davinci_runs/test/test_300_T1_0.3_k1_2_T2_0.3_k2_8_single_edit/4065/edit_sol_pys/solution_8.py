
n = int(input())
a = list(map(int, input().split()))

# dp[i] = max number of problems in a valid contest ending at a[i] (inclusive)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] * 2 >= a[i]:
            break
        dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
