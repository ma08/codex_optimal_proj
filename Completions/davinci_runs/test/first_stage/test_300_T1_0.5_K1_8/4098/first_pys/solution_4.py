

#-----Solution-----

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

dp = [1] * (n+1)
for i in range(1, n+1):
    for j in range(i-1, -1, -1):
        if a[i-1] - a[j] > 5:
            break
        dp[i] = max(dp[i], dp[j] + 1)

print(max(dp[i] for i in range(n+1)))