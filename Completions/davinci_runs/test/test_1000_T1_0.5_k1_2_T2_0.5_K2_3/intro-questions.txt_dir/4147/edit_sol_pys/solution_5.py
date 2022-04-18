
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
    if ls[cur] - 1 > 0 and a + ls[cur] - 1 <= A:
        res = min(res, dfs(cur + 1, a + ls[cur] - 1, b, c) + 9)
    if ls[cur] - 2 > 0 and a + ls[cur] - 2 <= A:
        res = min(res, dfs(cur + 1, a + ls[cur] - 2, b, c) + 8)
    if ls[cur] - 1 > 0 and b + ls[cur] - 1 <= B:
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 1, c) + 9)
    if ls[cur] - 2 > 0 and b + ls[cur] - 2 <= B:
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 2, c) + 8)
    if ls[cur] - 1 > 0 and c + ls[cur] - 1 <= C:
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 1) + 9)
    if ls[cur] - 2 > 0 and c + ls[cur] - 2 <= C:
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 2) + 8) 
    return res

print(dfs(0, 0, 0, 0))
