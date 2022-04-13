# coding: utf-8

H, W = map(int, input().split())  # 入力

for i in range(H):  # 出力
    print('#' + input() + '#')

print('#' * (W + 2))
