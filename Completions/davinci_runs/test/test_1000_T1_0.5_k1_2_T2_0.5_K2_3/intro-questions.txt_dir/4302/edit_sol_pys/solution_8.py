# coding: utf-8

# 入力
a, b = map(int, input().split())

# 入力された数値のうち大きい方を1回押す
print(a + b - max(a, b))
