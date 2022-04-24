
def main():
    N = int(input())
    s = input()
    l = len(s) + 1
    dp = [[0] * (N+1) for i in range(l)]
    dp[0][0] = 1
    for i in range(1, l):
        for j in range(N+1):
            if s[i-1] == '(':
                dp[i][j] += dp[i-1][j]
                if j < N:
                    dp[i][j+1] += dp[i-1][j]
            else:
                if j > 0:
                    dp[i][j-1] += dp[i-1][j]
    print(dp[l-1][0])

if __name__ == "__main__":
    main()
