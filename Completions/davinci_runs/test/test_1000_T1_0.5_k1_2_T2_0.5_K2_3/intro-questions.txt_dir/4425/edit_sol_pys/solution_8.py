
# 此题简单的解法是枚举，但是在有些情况下会超时，因此改用动态规划

def main():
    n, k = map(int, input().split())
    dp = [0] * (k+1)
    dp[k] = 1
    for i in range(k-1, 0, -1):
        dp[i] = dp[i+1] * (n-1) / n + (dp[i+1] + dp[i+2]) / 2 / n  # 两种情况，一种是猜中，一种是猜错
    print(dp[1])


if __name__ == '__main__':
    main()
