
import sys

def main():
    n = int(input())
    s = input()
    l = len(s)
    dp = [[0] * (n+1) for _ in range(l+1)]  # dp[i][j]: i文字目まで見て、閉じカッコがj個残っているときの場合の数
    ans = 0
    dp[0][0] = 1
    for i in range(l):
        for j in range(n):
            if dp[i][j] == 0:
                continue
            if s[i] == '(':
                dp[i+1][j] += dp[i][j]
                dp[i+1][j+1] += dp[i][j]
            else:
                if j > 0:
                    dp[i+1][j-1] += dp[i][j]
    for i in range(n+1):
        ans += dp[l][i]
    print(ans)

if __name__ == "__main__":
    main()
