from collections import defaultdict


def dfs(u, p, dp):
    for v in adj[u]:
        if v != p:
            dfs(v, u, dp)
            dp[u] += dp[v]


def solve(n, m, d):
    dp = [1] * (n + 1)
    global adj, dp
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    dfs(1, -1, dp)  # dp[i] is the number of nodes in the subtree of node i

    for i in range(1, n + 1):
        if dp[i] == d:
            break
    else:
        return "NO"

    ans = ["YES"]
    for u in range(2, n + 1):
        if dp[u] != d:
            ans.append(f'{1} {u}')

    return '\n'.join(ans)


def main():
    n, m, d = map(int, input().split())
    print(solve(n, m, d))


if __name__ == '__main__':
    main()
