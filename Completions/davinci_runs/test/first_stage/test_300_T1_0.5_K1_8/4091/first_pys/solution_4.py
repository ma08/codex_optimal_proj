

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # dp[i] = max profit for the first i problems,
    # where the last problem is the last problem of the last day
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        # [i - k, i] is the last k problems
        # dp[i - k - 1] is the max profit for the first i - k - 1 problems,
        # where the last problem is the last problem of the last day
        # dp[i - k] is the max profit for the first i - k problems,
        # where the last problem is the last problem of the last day
        # so dp[i - k - 1] <= dp[i - k]
        dp[i] = max(dp[i - k - 1], dp[i - k]) + max(a[i - k:i])

    # print(dp)
    print(dp[n])

    # reconstruct the order of the problems
    # that gives the max profit
    # (if there are multiple answers, this will be one of them)
    ans = []
    i = n
    while i > 0:
        if dp[i - 1] < dp[i]:
            ans.append(i - k)
            i -= k
        else:
            i -= 1
    ans.reverse()
    k = 0
    for i in range(1, len(ans)):
        print(ans[i] - ans[i - 1], end=' ')
    print(n - ans[-1])

if __name__ == '__main__':
    main()