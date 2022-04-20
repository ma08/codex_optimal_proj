

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # dp[i][j] = max profit if we use j days to solve the first i problems
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j == 1:
                dp[i][j] = sum(a[:i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1])

    print(dp[n][k])

    # backtrack to find the number of problems for each day
    ans = [0] * k
    x = n
    y = k
    while x > 0:
        if dp[x][y] == dp[x - 1][y]:
            x -= 1
        else:
            ans[y - 1] += 1
            x -= 1
            y -= 1

    print(*ans)

if __name__ == '__main__':
    main()
