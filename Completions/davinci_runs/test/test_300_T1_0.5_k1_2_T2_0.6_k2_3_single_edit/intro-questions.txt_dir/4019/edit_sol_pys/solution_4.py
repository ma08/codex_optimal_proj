
from collections import defaultdict



adj = defaultdict(list)
dp = []


def dfs(u, p):
    for v in adj[u]:
        if v != p:
            dfs(v, u)
            dp[u] += dp[v]


def solve(n, m, d):
    global adj, dp, ans
    adj.clear()
    dp = [1] * (n + 1)
    ans = []

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dfs(1, -1)

    for i in range(1, n + 1):
        if dp[i] == d:
            break
    else:
        return "NO"

    ans.append("YES")
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v and dp[v] != d:
                ans.append(f'{u} {v}')

    return '\n'.join(ans)


def main():
    n, m, d = map(int, input().split())
    for _ in range(int(input())):
        n, m, d = map(int, input().split())
        print(solve(n, m, d))


if __name__ == '__main__':
    main()
