n, k = map(int, input().split())
a = list(map(int, input().split()))


dp = [0] * (n + 1)  # dp[i]:=i番目までの要素を使って作れる最大の部分列の長さ
for i in range(1, n + 1):
    dp[i] = dp[i - 1]  # 今回の要素を使わない場合
    for j in range(i - 1, -1, -1):
        if a[i - 1] - a[j] <= 5:
            dp[i] = max(dp[i], dp[j] + i - j)  # 今回の要素を使う場合

print(max(dp[n - k + 1:]))
