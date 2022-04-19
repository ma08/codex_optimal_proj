

import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, read().split())) for _ in range(q)]
    abcd.sort(key=lambda x: x[1])
    dp = [[0] * m for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(m):
            dp[i][j] = dp[i-1][j]

    for a_i, b_i, c_i, d_i in abcd:
        for j in range(c_i, m):
            dp[b_i][j] = max(dp[b_i][j], dp[a_i][j-c_i] + d_i)

    print(max(dp[n]))

if __name__ == '__main__':
    main()
