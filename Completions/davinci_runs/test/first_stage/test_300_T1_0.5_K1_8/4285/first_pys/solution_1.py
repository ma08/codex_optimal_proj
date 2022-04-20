
import sys

def readline():
    return sys.stdin.readline()

def main():
    n = int(readline())
    s = readline()
    MOD = 10**9 + 7

    cnt = [0] * 26
    for c in s:
        if c == '?':
            cnt[ord(c) - ord('a')] += 1
        else:
            cnt[ord(c) - ord('a')] += 1
    # print(cnt)

    # dp[i][j][k] = the number of ways to insert i 'a's, j 'b's and k 'c's
    dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                if a < n:
                    dp[a+1][b][c] += dp[a][b][c]
                if b < n:
                    dp[a][b+1][c] += dp[a][b][c]
                if c < n:
                    dp[a][b][c+1] += dp[a][b][c]
                dp[a][b][c] %= MOD

    # print(dp)

    ans = dp[cnt[ord('a')-ord('a')]][cnt[ord('b')-ord('a')]][cnt[ord('c')-ord('a')]]
    print(ans)

if __name__ == '__main__':
    main()