import sys
sys.setrecursionlimit(10**6)


N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c, cost):
    if a == A and b == B and c == C:
        return cost
    if cur == N:
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c, cost))
    res = min(res, dfs(cur + 1, a + L[cur], b, c, cost + 10))
    res = min(res, dfs(cur + 1, a, b + L[cur], c, cost + 10))
    res = min(res, dfs(cur + 1, a, b, c + L[cur], cost + 10))
    if L[cur] - 1 >= 0:
        res = min(res, dfs(cur + 1, a + L[cur] - 1, b, c, cost + 9))
        res = min(res, dfs(cur + 1, a, b + L[cur] - 1, c, cost + 9))
        res = min(res, dfs(cur + 1, a, b, c + L[cur] - 1, cost + 9))
    if L[cur] - 2 >= 0:
        res = min(res, dfs(cur + 1, a + L[cur] - 2, b, c, cost + 8))
        res = min(res, dfs(cur + 1, a, b + L[cur] - 2, c, cost + 8))
        res = min(res, dfs(cur + 1, a, b, c + L[cur] - 2, cost + 8))
    return res

print(dfs(0, 0, 0, 0, 0))
