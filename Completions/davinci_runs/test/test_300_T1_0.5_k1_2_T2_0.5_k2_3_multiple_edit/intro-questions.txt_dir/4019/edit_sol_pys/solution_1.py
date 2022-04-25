
from collections import defaultdict


def dfs(u, p, d):
    for v, w in adj[u]:
        if v == p or w > d:
            continue
        dfs(v, u, d)
        dp[u] += dp[v]


def solve(n, m, d):
    adj = defaultdict(lambda: [])
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append((v, 1))
        adj[v].append((u, 1))

    dp = [1] * (n + 1)
    dfs(1, -1, d)

    for i in range(1, n + 1):
        if dp[i] == d:
            break
    else:
        return "NO"

    ans = ["YES"]
    for u in range(1, n + 1):
        for v, w in adj[u]:
            if u < v and dp[v] != d and w == 1:
                ans.append(f'{u} {v} 1')

    return '\n'.join(ans)


def main():
    n, m, d = map(int, input().split())
    print(solve(n, m, d))


if __name__ == '__main__':
    main()
