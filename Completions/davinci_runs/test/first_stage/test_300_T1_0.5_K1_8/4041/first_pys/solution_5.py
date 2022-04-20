

import sys

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    len_s = len(s)
    len_t = len(t)
    # dp[i][j] means the max length of substring of s[0:i] and t[0:j]
    dp = [[0 for j in range(len_t + 1)] for i in range(len_s + 1)]
    for i in range(len_s + 1):
        for j in range(len_t + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(len_s - dp[len_s][len_t])

if __name__ == "__main__":
    main()