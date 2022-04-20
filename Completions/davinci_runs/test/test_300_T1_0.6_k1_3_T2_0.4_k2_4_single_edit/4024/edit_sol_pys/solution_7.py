
import sys
sys.setrecursionlimit(10**6)


def dfs(i, n, k, s, memo):
    if memo[i][k] != -1: return memo[i][k]

    if k == 0: return 0

    # if we don't use s[i]
    res = dfs(i + 1, n, k, s, memo)

    # if we use s[i]
    if i + 1 <= n and s[i] != s[i + 1]: res = min(res, dfs(i + 1, n, k - 1, s, memo))

    memo[i][k] = res
    return res


def solve(n, k, s):
    memo = [[-1] * (k + 1) for _ in range(n + 1)]
    ans = dfs(0, n, k, s, memo)
    if ans >= 10**9: return -1
    return ans


def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(solve(n, k, s))


if __name__ == "__main__":
    main()
