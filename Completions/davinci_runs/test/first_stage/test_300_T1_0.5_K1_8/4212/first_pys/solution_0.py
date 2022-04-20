

n, m, q = map(int, input().split())

# 入力
abcd = []
for i in range(q):
    a, b, c, d = map(int, input().split())
    abcd.append([a, b, c, d])

# スコア計算
score = 0
for i in range(q):
    a, b, c, d = abcd[i]
    if b - a == c:
        score += d

# 出力
print(score)