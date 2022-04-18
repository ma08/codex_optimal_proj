# -*- coding: utf-8 -*-

N = int(input())  # 入力

s = 0  # 初期化
for i in range(N):
    l, r = map(int, input().split())  # スペース区切りで入力を分ける
    s += r - l + 1

print(s)  # 結果出力
