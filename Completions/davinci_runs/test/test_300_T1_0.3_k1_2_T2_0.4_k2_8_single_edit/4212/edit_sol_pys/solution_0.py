# 入力
N = int(input())
A = list(map(int, input().split()))


# 初期化
ans = 0

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
