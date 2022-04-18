

def main():
    n, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    dp = [[0 for i in range(k)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(k):  # j: 和
            for r in range(k):  # r: 前一个数的和
                dp[i][j] = max(dp[i][j], dp[i - 1][r] + matrix[i - 1][(j - r) % k])
    print(max(dp[n]))

if __name__ == "__main__":
    main()
