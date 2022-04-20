

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = max(dp[i], a[i])

for i in range(n-1, -1, -1):
    dp[i] = max(dp[i], dp[i+1])

dp = [0] + dp

dp2 = [0] * (n+1)
for i in range(1, n+1):
    dp2[i] = dp2[i-1] + dp[i]

if k == 1:
    print(dp2[n])
    print(n)
else:
    dp = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            dp[i] = max(dp[i], dp2[j] - dp2[i-1])
    dp = [0] + dp

    dp2 = [0] * (n+1)
    for i in range(1, n+1):
        dp2[i] = dp2[i-1] + dp[i]

    dp = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            dp[i] = max(dp[i], dp2[j] - dp2[i-1])
    dp = [0] + dp

    dp2 = [0] * (n+1)
    for i in range(1, n+1):
        dp2[i] = dp2[i-1] + dp[i]

    dp = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            dp[i] = max(dp[i], dp2[j] - dp2[i-1])
    dp = [0] + dp

    for i in range(n-1, -1, -1):
        dp[i] = max(dp[i], dp[i+1])

    print(dp[1])

    curr = 1
    while k > 0:
        if k == 1:
            print(n-curr+1)
            break
        else:
            for i in range(curr+1, n+1):
                if dp[curr] == dp[i+1] + dp2[i] - dp2[curr-1]:
                    print(i-curr+1)
                    curr = i+1
                    k -= 1
                    break