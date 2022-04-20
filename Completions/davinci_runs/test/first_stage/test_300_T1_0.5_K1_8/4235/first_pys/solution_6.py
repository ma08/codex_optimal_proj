


def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * (n+1)
    visited[1] = True
    q = [1]
    while q:
        u = q.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    if any(not visited[i] for i in range(1, n+1)):
        print("NO")
        return
    print("YES")
    for i in range(1, n+1):
        for v in adj[i]:
            if v > i:
                print(0, end="")
    for i in range(1, n+1):
        for v in adj[i]:
            if v < i:
                print(1, end="")


if __name__ == "__main__":
    main()