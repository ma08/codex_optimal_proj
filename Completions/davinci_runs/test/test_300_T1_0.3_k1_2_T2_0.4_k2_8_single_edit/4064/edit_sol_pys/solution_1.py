
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

def solve(n, h, l, r, a):
    dp = [0] * (h + 1)
    dp[0] = 0
    for i in range(n):
        dp2 = [0] * (h + 1)
        for j in range(h + 1):
            dp2[j] = dp[j]
            if j >= a[i]:
                dp2[j] = max(dp2[j], dp[j - a[i]])
            if j >= a[i] - 1:
                dp2[j] = max(dp2[j], dp[j - a[i] + 1])
            if l <= j <= r:
                dp2[j] += 1
        dp = dp2[:]
    return max(dp)

print(solve(n, h, l, r, a))
