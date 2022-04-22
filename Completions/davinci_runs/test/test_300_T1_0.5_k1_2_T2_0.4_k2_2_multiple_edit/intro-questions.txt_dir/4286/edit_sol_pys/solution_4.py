from collections import deque


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x].append((y, w))
        g[y].append((x, w))

    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v, w in g[u]:
            if dp[v] > dp[u] + w:
                dp[v] = dp[u] + w
                q.append(v)

    ans = sum(a)
    for i in range(2, n + 1):
        ans += min(dp[i], a[i - 1])

    print(ans)


if __name__ == '__main__':
    main()
