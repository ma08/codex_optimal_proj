

def main():
    """
    dp[i][j] = true if the string from i...j is sortable
    dp[i][i] = true
    dp[i][j] = (dp[i][k] and dp[k + 1][j] and s[i] < s[j]) or (dp[i][k] and dp[k + 1][j] and s[i] > s[j]) or (dp[i][k] and dp[k + 1][j] and s[k] < s[k + 1])
    """
    n = int(input())
    s = input()
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                dp[i][j] = dp[i][j] or (dp[i][k] and dp[k + 1][j] and s[i] < s[j]) or (dp[i][k] and dp[k + 1][j] and s[i] > s[j]) or (dp[i][k] and dp[k + 1][j] and s[k] > s[k + 1])
    if not dp[0][n - 1]:
        print("NO")
        return
    print("YES")
    res = [0] * n
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                res[i] = 0
                res[j] = 1
                break
    print("".join(map(str, res)))

if __name__ == "__main__":
    main()
