
N, A, B, C = map(int, input().split())
ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c, cost):
    if a == A and b == B and c == C: # 全ての木を使った
        return 0
    if cur == N: # 全ての木を使っていない
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c, cost)) # 使わない
    res = min(res, dfs(cur + 1, a + ls[cur], b, c, cost) + 10) # Aに使う
    res = min(res, dfs(cur + 1, a, b + ls[cur], c, cost) + 10) # Bに使う
    res = min(res, dfs(cur + 1, a, b, c + ls[cur], cost) + 10) # Cに使う
    if a == 0: # Aに使わない
        res = min(res, dfs(cur + 1, a + ls[cur] - 1, b, c, cost) + 10)
    if b == 0: # Bに使わない
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 1, c, cost) + 10)
    if c == 0: # Cに使わない
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 1, cost) + 10)
    if a == 0: # Aに使わない
        res = min(res, dfs(cur + 1, a + ls[cur] - 2, b, c, cost) + 10)
    if b == 0: # Bに使わない
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 2, c, cost) + 10)
    if c == 0: # Cに使わない
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 2, cost) + 10)
    return res

print(dfs(0, 0, 0, 0, 0))
