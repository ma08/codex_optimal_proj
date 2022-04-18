
import sys
sys.setrecursionlimit(10**6)


def dfs(i, n, k, s, cost, memo, used):
    if memo[i][k] != -1:
        return 0
    if i == n:
        return memo[i][k]

    if k == 0:
        return 0

    # if we don't use s[i]
    res = dfs(i + 1, n, k, s, cost, memo, used)

    # if we use s[i]
    if i + 1 <= n and s[i] != s[i + 1] and not used[i]:
        used[i] = True
        res = min(res, cost[i + 1] + dfs(i + 1, n, k - 1, s, cost, memo, used))
        used[i] = False

    memo[i][k] = res
    return res


    used = [False] * (n + 1)
def solve(n, k, s):
    cost = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        cost[i] = cost[i + 1] + (n - i)

    memo = [[-1] * (k + 1) for _ in range(n + 1)]
    ans = dfs(0, n, k, s, cost, memo, used)
    if ans >= 10**9:
        return -1
    return ans


def main():
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))


if __name__ == "__main__":
    main()
