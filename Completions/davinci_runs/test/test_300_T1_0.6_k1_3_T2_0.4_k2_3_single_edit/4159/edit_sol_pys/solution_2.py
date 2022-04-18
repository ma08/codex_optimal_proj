

a, b, k = map(int, input().split())  # 入力

for i in range(k):  # k回
    if a > 0:  # aが0以上なら
        a -= 1  # aを減らす
    elif b > 0:  # aが0以下でbが0以上なら
        b -= 1  # bを減らす

print(a, b)  # 出力
