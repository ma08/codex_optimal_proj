def main():
    N, M = [int(i) for i in input().split()]
    dp = [0] * (N + 1)

    # ダメな段
    a = set()
    for i in range(M):
        ai = int(input())
        a.add(ai)

    # 初期化
    dp[0] = 1
    if 1 not in a:
        dp[1] = 1

    # dp[i] → dp[i + 1] の更新
    for i in range(N):
        if i + 1 not in a:
            dp[i + 1] = (dp[i + 1] + dp[i]) % (10 ** 9 + 7)
        if i + 2 not in a:
            dp[i + 2] = (dp[i + 2] + dp[i]) % (10 ** 9 + 7)

    print(dp[N])


if __name__ == '__main__':
    main()
