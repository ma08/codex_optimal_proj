
from collections import defaultdict


def dfs(u, p):
    for v in adj[u]:
        if v != p:
            dfs(v, u)
            dp[u] += dp[v]
    dp = [1] * (n + 1)
    ans = []


def solve(n, m, k):
    global adj, dp, ans
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dfs(1, -1)

    for i in range(1, n + 1):
        if dp[i] == k:
            break
    else:
        return "NO"

    ans.append("YES")
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v and dp[v] != k:
                ans.append(f'{u} {v}')

    return '\n'.join(ans)


def main():
    n, m, k = map(int, input().split())
    print(solve(n, m, k))


if __name__ == '__main__':
    main()
