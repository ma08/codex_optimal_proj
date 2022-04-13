
# https://codeforces.com/problemset/problem/1343/B

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x].append((y, w))
        g[y].append((x, w))

    spf = [float('inf')] * (n + 1)
    spf[1] = 0
    q = [1]
    while q:
        u = q.pop(0)
        for v, w in g[u]:
            if spf[v] > spf[u] + w:
                spf[v] = spf[u] + w
                q.append(v)

    ans = sum(a)
    for i in range(2, n + 1):
        ans += min(spf[i], a[i - 1])

    print(ans)


if __name__ == '__main__':
    main()
