#
#
#
#


n, k = map(int, input().split()) #n, k값 입력 받기
a = sorted(list(map(int, input().split()))) #a값 입력 받기

dp = [0] * (n + 1) #dp리스트 생성
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    for j in range(i - 1, -1, -1):
        if a[i - 1] - a[j] <= 5:
            dp[i] = max(dp[i], dp[j] + i - j)

ans = 0
for i in range(n, n - k, -1):
    ans = max(ans, dp[i])
print(ans)
