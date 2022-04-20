

import sys

def main():
    # input
    N, M, Q = map(int, sys.stdin.readline().strip().split())
    abcd = []
    for _ in range(Q):
        abcd.append(tuple(map(int, sys.stdin.readline().strip().split())))

    # initialize
    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][0]
        for j in range(1, M+1):
            dp[i][j] = dp[i][j-1]
            for a, b, c, d in abcd:
                if i == b and j == c:
                    dp[i][j] = max(dp[i][j], dp[a-1][c] + d)

    # output
    print(dp[-1][-1])

if __name__ == '__main__':
    main()