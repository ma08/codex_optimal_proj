

# 入力例
# 5 2 3
# 1 5 2 1
# 2 5 1 2
# 3 5 1 1
N, M, Q = map(int, input().split())  # 5 2 3
abcd = [list(map(int, input().split())) for i in range(Q)]  # 1 5 2 1  2 5 1 2  3 5 1 1
# [[1, 5, 2, 1], [2, 5, 1, 2], [3, 5, 1, 1]]

# 全探索
ans = 0
for i in range(2 ** N):
    # 各桁で1が立っているかどうか
    A = [0] * N
    for j in range(N):
        if (i >> j) & 1:
            A[j] = 1

    # 各クエリについて確認
    score = 0
    for a, b, c, d in abcd:
        a -= 1
        b -= 1
        if A[b] - A[a] == c:
            score += d
    ans = max(ans, score)

# 出力
print(ans)
