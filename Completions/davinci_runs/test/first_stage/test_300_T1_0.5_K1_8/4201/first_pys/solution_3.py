

import sys

H, W, K = map(int, input().split())

# 縦横に切る線が何本か
cut_lines = H + W - 1

# 切る線の数と黒いマスの数から、切る線のうち何本を使うかを全探索
# 全探索の個数は、切る線の数から黒いマスの数を引いた数の二項係数
# これを全探索の個数として、その中で黒いマスの数がK個になるものを数える

# 二項係数を求める関数
def combination(n, k):
    res = 1
    for i in range(k):
        res *= (n-i)
        res //= (i+1)
    return res

# 全探索の個数
all_num = combination(cut_lines, K)

# 全探索の個数から、K個のマスになるものを数える
res = 0
for i in range(K+1):
    # 全探索の個数のうち、i個の縦線を使ったものを数える
    num = combination(H-1, i)
    # i個の縦線を使ったもののうち、K-i個の横線を使ったものを数える
    if K-i <= W-1:
        num *= combination(W-1, K-i)
        res += num

print(res)