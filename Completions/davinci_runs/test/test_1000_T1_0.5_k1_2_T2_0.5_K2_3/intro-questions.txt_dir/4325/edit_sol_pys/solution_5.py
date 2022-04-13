
# 何個入っているか、何個入れられるか、何分かかるかを受け取る
n, x, t = map(int, input().split())  # 受け取った値をint型に変換してn, x, tに代入

if n % x == 0:  # nをxで割り切れる時
    print(t * (n // x))  # tをnをxで割った値で掛ける
else:
    print(t * (n // x + 1))
