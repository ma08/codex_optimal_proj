

N, A, B, C = map(int, input().split()) # 入力
ls = [int(input()) for _ in range(N)] # 入力

def dfs(cur, a, b, c): # 深さ優先探索
    if a == A and b == B and c == C: # 全ての長さが揃ったら終了
        return 0
    if cur == N: # 全ての木を見終わったら終了
        return float('inf')
    res = float('inf') # 最小値を求めるために初期値をinfにする
    res = min(res, dfs(cur + 1, a, b, c))
    res = min(res, dfs(cur + 1, a + ls[cur], b, c) + 10) # aに加える
    res = min(res, dfs(cur + 1, a, b + ls[cur], c) + 10) # bに加える
    res = min(res, dfs(cur + 1, a, b, c + ls[cur]) + 10) # cに加える
    if ls[cur] - 1 >= 0: # 木の長さが1以上なら
        res = min(res, dfs(cur + 1, a + ls[cur] - 1, b, c) + 9) # aに加える
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 1, c) + 9) # bに加える
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 1) + 9) # cに加える
    if ls[cur] - 2 >= 0: # 木の長さが2以上なら
        res = min(res, dfs(cur + 1, a + ls[cur] - 2, b, c) + 8) # aに加える
        res = min(res, dfs(cur + 1, a, b + ls[cur] - 2, c) + 8) # bに加える
        res = min(res, dfs(cur + 1, a, b, c + ls[cur] - 2) + 8) # cに加える
    return res # 答えを返す

print(dfs(0, 0, 0, 0)) # 実行
