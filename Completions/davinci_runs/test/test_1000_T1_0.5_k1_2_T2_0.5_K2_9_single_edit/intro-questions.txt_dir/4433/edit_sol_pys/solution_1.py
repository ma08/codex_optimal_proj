


def solution(n, m, edges):
    """
    >>> solution(5, 5, [[1, 2], [2, 3], [3, 5], [4, 3], [1, 5]])
    [[3, 5], [2, 1], [3, 2], [3, 4]]
    """
    ans = [0] * m
    visited = [False] * n
    adj = [[] for _ in range(n)]
    for v, u in edges:
        adj[v - 1].append(u - 1)
        adj[u - 1].append(v - 1)
    q = collections.deque([0])
    visited[0] = True
    while q:
        v = q.popleft()
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
                ans.append(v)
                ans.append(u)
    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    ans = solution(n, m, edges)
    print(ans)
