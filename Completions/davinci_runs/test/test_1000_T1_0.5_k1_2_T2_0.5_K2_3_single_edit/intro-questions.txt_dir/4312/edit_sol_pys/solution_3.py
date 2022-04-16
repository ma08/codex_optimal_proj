# -*- coding: utf-8 -*-

# 入力
A,B,C,D = map(int, input().split())

# 先手必勝かどうか
if (A <= C and B < D) or (A < C and B <= D):
    print("No")
else:
    print("Yes")
