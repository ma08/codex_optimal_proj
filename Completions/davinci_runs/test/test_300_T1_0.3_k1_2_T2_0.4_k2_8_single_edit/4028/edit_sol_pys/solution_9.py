
import sys

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

def solve(n):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(i + 1):
            if i + j + 1 <= n:
                dp[i + j + 1] += dp[i]
                dp[i + j + 1] %= MOD
    return dp[n]

if __name__ == '__main__':
    main()
