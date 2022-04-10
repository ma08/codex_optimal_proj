

#-----Solution-----

n = int(input())
a = list(map(int, input().split()))

dp = [[0, 0] for i in range(n)]

for i in range(n):
    if i == 0:
        dp[i][0] = 1
        dp[i][1] = 1
    else:
        if a[i] > a[i - 1]:
            dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = 1
        if a[i] > a[i - 1]:
            dp[i][1] = 1
        else:
            dp[i][1] = dp[i - 1][1] + 1

max_dp = max(dp[n - 1])

if max_dp == 1:
    print(1)
    print("R")
else:
    print(max_dp)
    ans = ""
    i = n - 1
    while i > 0:
        if dp[i][0] == max_dp:
            ans = "L" + ans
            i -= 1
            max_dp -= 1
        else:
            ans = "R" + ans
            i -= 1
            max_dp -= 1
    if i == 0:
        ans = "L" + ans
    print(ans)