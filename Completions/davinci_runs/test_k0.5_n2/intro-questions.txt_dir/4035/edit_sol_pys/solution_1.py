from math import floor

a, b = map(int, input().split())  # 入力を受け取る

for i in range(1, 101):  # 1から100までループ
    if floor(i * 0.08) == a and floor(i * 0.1) == b:  # 小数点を切り捨てて比較
        print(i)  # 答えを出力
        exit()  # 終了

print(-1)
