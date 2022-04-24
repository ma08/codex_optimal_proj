
def main():
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if mat[i][j] == 0:
                continue

            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
