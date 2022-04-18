N, A, B, C = map(int, input().split())


ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c, cost):
    if a == 0 and b == 0 and c == 0:
        return cost
    if cur == N:
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c, cost))
    if a + ls[cur] <= A:
        res = min(res, dfs(cur + 1, a + ls[cur], b, c, cost + 10))
    if b + ls[cur] <= B:
        res = min(res, dfs(cur + 1, a, b + ls[cur], c, cost + 10))
    if c + ls[cur] <= C:
        res = min(res, dfs(cur + 1, a, b, c + ls[cur], cost + 10))
    if a + ls[cur] - 1 <= A:
        res = min(res, dfs(cur + 1, a + ls[cur] - 1, b, c, cost + 9)) 
    if a + ls[cur] - 2 <= A:
        res = min(res, dfs(cur + 1, a + ls[cur] - 2, b, c, cost + 8)) 
    if b + ls[cur] - 1 <= B:
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 1, c, cost + 9)) 
    if b + ls[cur] - 2 <= B:
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 2, c, cost + 8)) 
    if c + ls[cur] - 1 <= C:
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 1, cost + 9)) 
    if c + ls[cur] - 2 <= C:
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 2, cost + 8)) 
    return res

print(dfs(0, 0, 0, 0, 0))
