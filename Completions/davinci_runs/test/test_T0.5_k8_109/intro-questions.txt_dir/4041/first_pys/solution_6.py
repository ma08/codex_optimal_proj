

def main():
    s = input()
    t = input()

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    print(len(s) - dp[0][0])

if __name__ == '__main__':
    main()