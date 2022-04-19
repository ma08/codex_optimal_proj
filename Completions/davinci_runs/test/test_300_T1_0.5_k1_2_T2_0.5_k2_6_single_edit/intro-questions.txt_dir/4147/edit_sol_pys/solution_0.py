N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]



def dfs(cur, a, b, c, cost):
    if a > A or b > B or c > C:
        return float('inf')
    if cur == N:
        if a == A and b == B and c == C:
            return cost
        return 0
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c, cost))
    res = min(res, dfs(cur + 1, a + l[cur], b, c, cost + 10))
    res = min(res, dfs(cur + 1, a, b + l[cur], c, cost + 10))
    res = min(res, dfs(cur + 1, a, b, c + l[cur], cost + 10))
    if l[cur] - 1 > 0:
        res = min(res, dfs(cur + 1, a + l[cur] - 1, b, c, cost + 9))
        res = min(res, dfs(cur + 1, a, b + l[cur] - 1, c, cost + 9))
        res = min(res, dfs(cur + 1, a, b, c + l[cur] - 1, cost + 9))
    if l[cur] - 2 > 0:
        res = min(res, dfs(cur + 1, a + l[cur] - 2, b, c, cost + 8))
        res = min(res, dfs(cur + 1, a, b + l[cur] - 2, c, cost + 8))
        res = min(res, dfs(cur + 1, a, b, c + l[cur] - 2, cost + 8))
    return res


print(dfs(0, 0, 0, 0, 0))
