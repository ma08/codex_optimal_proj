
def min_edit_distance(s, t):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (s[i - 1] != t[j - 1]))
    return dp[n][n]

def main():
    s = input()
    t = input()
    print(min_edit_distance(s, t))

if __name__ == '__main__':
    main()