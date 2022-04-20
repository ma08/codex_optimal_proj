
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(solve(s))

def solve(s):
    MOD = 1000000007
    dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = 1
    for i in range(1, len(s) + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < i:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD
    return dp[len(s)][s.count('(') - s.count(')')]

if __name__ == '__main__':
    main()
