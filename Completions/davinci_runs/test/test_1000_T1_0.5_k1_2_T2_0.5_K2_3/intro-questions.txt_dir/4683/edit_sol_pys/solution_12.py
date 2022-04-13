
# coding: utf-8
N = int(input())  # 入力
A = list(map(int, input().split()))  # 入力
count = 0  # 初期化
for i in range(N - 1):  # ループ
    for j in range(i + 1, N):  # ループ
        count += A[i] * A[j]  # 計算
print(count % (10 ** 9 + 7))  # 出力
