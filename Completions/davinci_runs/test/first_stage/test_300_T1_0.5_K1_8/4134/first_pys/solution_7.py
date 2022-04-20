

import sys

def read_line():
    return sys.stdin.readline().strip()

def read_ints():
    return [int(x) for x in read_line().split()]

def read_int():
    return read_ints()[0]

def read_grid(n, m):
    return [read_ints() for _ in range(n)]

def solve(n, m, k, a):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    for i in range(n):
        for j in range(m):
            dp[i][j] = dp[i][j] if a[i][j] ^ k == 0 else 0
    return dp[n - 1][m - 1]

def main():
    n, m, k = read_ints()
    a = read_grid(n, m)
    print(solve(n, m, k, a))

if __name__ == '__main__':
    main()