
import sys
sys.setrecursionlimit(10**6)


def dfs(i, n, k, s, cost, memo):
    if memo[i][k] != -1:
        return memo[i][k]

    if k == 0:
        return 0

    # if we don't use s[i]
    res = dfs(i + 1, n, k, s, cost, memo)

    # if we use s[i]
    if i + 1 <= n and s[i] == s[i + 1]:
        res = min(res, cost[i] + dfs(i + 1, n, k - 1, s, cost, memo))

    memo[i][k] = res
    return res


def solve(n, k, s):
    cost = [0] * n
    for i in range(n):
        cost[i] = i + 1

    memo = [[-1] * (k + 1) for _ in range(n + 1)]
    ans = dfs(0, n, k, s, cost, memo)
    if ans >= 10**9:
        return -1
    return ans


def main():
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))


if __name__ == "__main__":
    main()
