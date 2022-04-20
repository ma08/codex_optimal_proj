
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(solve(n, s))

def solve(n, s):
    MOD = 1000000007
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][0] = 1
    for i in range(n):
        dp[(i + 1) % 2] = [0] * (n + 1)
        for j in range(n + 1):
            if j > 0: dp[(i + 1) % 2][j - 1] += dp[i % 2][j]
            if j < n: dp[(i + 1) % 2][j + 1] += dp[i % 2][j]
            dp[(i + 1) % 2][j] %= MOD
    return dp[n % 2][s.count('(') - s.count(')')]

if __name__ == '__main__':
    main()
