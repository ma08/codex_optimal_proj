
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(solve(n, s))

def solve(n, s):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if s[i - 1] == '(':
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] * 2
            if i >= 2:
                dp[i] -= dp[i - 2]
            dp[i] %= MOD
    return dp[n]

if __name__ == '__main__':
    main()
