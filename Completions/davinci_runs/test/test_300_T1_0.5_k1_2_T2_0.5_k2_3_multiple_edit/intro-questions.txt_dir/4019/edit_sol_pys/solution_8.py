
from collections import defaultdict


def dfs(v, p):
    for u in adj[v]:
        if v != p:
            dfs(u, v)
            dp[v] += dp[u]


def solve(n, m, d):
    global adj, dp
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dp = [0] * (n + 1)
    dfs(1, 0)

    for i in range(1, n + 1):
        if dp[i] == d - 1:
            break
    else:
        return "NO"

    ans = ["YES"]
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v and dp[v] != d - 1:
                ans.append(f'{u} {v}')

    return '\n'.join(ans)


def main():
    n, m, d = map(int, input().split())
    print(solve(n, m, d))


if __name__ == '__main__':
    main()
