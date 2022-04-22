import sys
sys.setrecursionlimit(10**6)

def dfs(n, m, q, abcd, i, j, dp):
    if j == m:
        return 0
    if i == n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    ret = dfs(n, m, q, abcd, i+1, j, dp)
    for a, b, c, d in abcd:
        if a <= i and b > i:
            ret = max(ret, dfs(n, m, q, abcd, i+1, j+c, dp) + d)
    dp[i][j] = ret
    return ret


def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    abcd.sort(key=lambda x: (x[1], x[0]))
    # print(abcd)
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    print(dfs(n, m, q, abcd, 1, 0, dp))

if __name__ == '__main__':
    main()
