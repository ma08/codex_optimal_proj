from collections import defaultdict

def dfs(u, p):
    for v in adj[u]:
        if v != p:
            dfs(v, u)
            dp[u] += dp[v]


def solve(n, m, d):
    global adj, dp, ans
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dp = [1] * (n + 1)
    dfs(1, -1)

    for i in range(1, n + 1):
        if dp[i] == d:
            break
    else:
        return "NO"

        return "NO"

    ans = []
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v and dp[v] != d:
                ans.append(f'{u} {v}')

    return "YES\n" + '\n'.join(ans)


def main():
    n, m, d = map(int, input().split())
    print(solve(n, m, d))


if __name__ == '__main__':
    main()
