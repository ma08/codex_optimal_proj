

n = int(input())
a = list(map(int, input().split()))
a = [0] + a
a.sort()


def solve(n, a):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1


    for i in range(2, n+1):
        dp[i] = dp[i-1]
        if a[i-1] > a[i-2]:
            dp[i] += 1

    return dp[n]

print(solve(n, a))
