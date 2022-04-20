
N, A, B, C = map(int, input().split())
ls = [int(input()) for _ in range(N)]

def dfs(cur, a, b, c, cost):
    if a == A and b == B and c == C: # すべての材料が揃ったら終了
        return 0
    if cur == N: # 全ての材料を使い切ったら終了
        return float('inf')
    res = float('inf')
    res = min(res, dfs(cur + 1, a, b, c, cost)) # 全く使わない
    res = min(res, dfs(cur + 1, a + ls[cur], b, c, cost + 10)) # Aに使う
    res = min(res, dfs(cur + 1, a, b + ls[cur], c, cost + 10)) # Bに使う
    res = min(res, dfs(cur + 1, a, b, c + ls[cur], cost + 10)) # Cに使う
    if ls[cur] - 1 > 0: # 1つ減らして使う
        res = min(res, dfs(cur + 1, a + ls[cur] - 1, b, c, cost + 9)) # Aに使う
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 1, c, cost + 9)) # Bに使う
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 1, cost + 9)) # Cに使う
    if ls[cur] - 2 > 0: # 2つ減らして使う
        res = min(res, dfs(cur + 1, a + ls[cur] - 2, b, c, cost + 8)) # Aに使う
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 2, c, cost + 8)) # Bに使う
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 2, cost + 8)) # Cに使う
    return res

print(dfs(0, 0, 0, 0, 0))
