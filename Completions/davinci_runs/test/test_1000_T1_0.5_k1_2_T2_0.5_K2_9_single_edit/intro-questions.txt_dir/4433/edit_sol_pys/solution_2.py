import collections

def solution(n, m, edges):
    ans = []
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
                ans.append([v + 1, u + 1])
    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    ans = solution(n, m, edges)
    for v, u in ans:
        print(v, u)
