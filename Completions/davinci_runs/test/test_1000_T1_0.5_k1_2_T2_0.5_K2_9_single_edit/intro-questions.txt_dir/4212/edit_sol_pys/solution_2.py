

def main():
    n, m, q = map(int, input().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(q):
        a, b, c, d = map(int, input().split())
        for i in range(a-1, b):
            for j in range(c-1, m):
                dp[i][j] = max(dp[i][j], dp[i][j-c] + d)

    print(max(map(max, dp)))

if __name__ == '__main__':
    main()
