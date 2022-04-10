

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(sum(a))
    print(n)
else:
    score = [0] * n
    for i in range(n - k + 1):
        score[i] = max(a[i:i + k])

    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + score[i]

    dp = [0] * (n + 1)
    for i in range(2, k + 1):
        for j in range(i, n + 1):
            dp[j] = max(dp[j - 1], s[j] - s[j - i])

    print(dp[n])
    j = n
    for i in range(k, 0, -1):
        while j >= i and dp[j] == dp[j - 1]:
            j -= 1
        print(j - (n - j) + 1, end=' ')
        j -= 1