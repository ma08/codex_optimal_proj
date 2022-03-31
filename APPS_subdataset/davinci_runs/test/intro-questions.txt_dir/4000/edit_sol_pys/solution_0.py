
def main():
    n = int(input())
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    def dfs(v, p=None):
        ret = 1
        for u in adj[v]:
            if u == p:
                continue
            ret += dfs(u, v)
        return ret

    def solve():
        a, b = None, None
        for i in range(n):
            if len(adj[i]) == 1:
                a = i
                break
        for i in range(n):
            if len(adj[i]) == 1:
                b = i
                break
        if a is None or b is None:
            return -1, -1, -1
        return a, b, n - dfs(a) - dfs(b)

    a, b, c = solve()
    print(c)
    print(a, b, c)


if __name__ == "__main__":
    main()
