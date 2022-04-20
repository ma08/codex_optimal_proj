n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

def solve(n, h, l, r, a):
    dp = [0] * h
    dp[0] = 1
    for i in range(1, h):
        dp[i] = dp[i-1]
        if i >= a[0]:
            dp[i] = max(dp[i], dp[i-a[0]])
    for i in range(1, n):
        dp2 = [0] * h
        dp2[0] = 1
        for j in range(1, h):
            dp2[j] = dp2[j-1]
            if j >= a[i]:
                dp2[j] = max(dp2[j], dp2[j-a[i]])
            if j >= a[i] - 1:
                dp2[j] = max(dp2[j], dp[j-a[i]+1])
        dp = dp2
    return sum(dp[l:r+1])

print(solve(n, h, l, r, a))

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

def solve(n, h, l, r, a):
    dp = [0] * h
    dp[0] = 1
    for i in range(1, h):
        dp[i] = dp[i-1]
        if i >= a[0]:
            dp[i] = max(dp[i], dp[i-a[0]])
    for i in range(1, n):
        dp2 = [0] * h
        dp2[0] = 1
        for j in range(1, h):
            dp2[j] = dp2[j-1]
            if j >= a[i]:
                dp2[j] = max(dp2[j], dp2[j-a[i]])
            if j >= a[i] - 1:
                dp2[j] = max(dp2[j], dp[j-a[i]+1])
        dp = dp2
    return sum(dp[l:r+1])

print(solve(n, h, l, r, a))
