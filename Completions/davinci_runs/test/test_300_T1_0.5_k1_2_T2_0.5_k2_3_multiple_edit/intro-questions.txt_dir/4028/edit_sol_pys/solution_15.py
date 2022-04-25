import sys

def main():
    n = int(input())
    s = input()
    l = len(s)
    dp = [[0] * (n + 1) for _ in range(l + 1)]
    for i in range(l):
        if s[i] == '(':
            dp[i][0] = 1
    for i in range(l + 1):
        for j in range(n + 1):
            if dp[i][j] == 0:
                continue
            if s[i] == '(':
                dp[i+1][j] += dp[i][j]
                dp[i+1][j+1] += dp[i][j]
            else:
                if j > 0:
                    dp[i+1][j-1] += dp[i][j]
    print(dp[l][0])

if __name__ == "__main__":
    main()
