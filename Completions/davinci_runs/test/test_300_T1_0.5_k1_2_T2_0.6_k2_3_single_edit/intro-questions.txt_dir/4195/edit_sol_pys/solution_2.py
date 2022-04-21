# coding: utf-8


D, N = map(int, input().split()) # 入力

if N == 100:
    N += 1

if D == 0: # Dが0の時
    print(N) # Nを出力
elif D == 1: # Dが1の時
    print(100 * N) # 100 * Nを出力
else:
    print(10000 * N) # 10000 * Nを出力
