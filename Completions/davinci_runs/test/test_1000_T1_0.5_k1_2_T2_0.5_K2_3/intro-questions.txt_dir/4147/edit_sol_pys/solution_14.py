
N, A, B, C = map(int, input().split())
ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c):
    if a == A and b == B and c == C:
        return 0
    if cur == N:
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c))
    res = min(res, dfs(cur + 1, a + ls[cur], b, c) + 10)
    res = min(res, dfs(cur + 1, a, b + ls[cur], c) + 10)
    res = min(res, dfs(cur + 1, a, b, c + ls[cur]) + 10)
    if a > 0:
        res = min(res, dfs(cur + 1, a - 1, b, c) + 9)
    if b > 0:
        res = min(res, dfs(cur + 1, a, b - 1, c) + 9)
    if c > 0:
        res = min(res, dfs(cur + 1, a, b, c - 1) + 9)
    if a > 1:
        res = min(res, dfs(cur + 1, a - 2, b, c) + 8)
    if b > 1:
        res = min(res, dfs(cur + 1, a, b - 2, c) + 8)
    if c > 1:
        res = min(res, dfs(cur + 1, a, b, c - 2) + 8)
    return res

print(dfs(0, 0, 0, 0))
