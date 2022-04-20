import numpy as np

import sys

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 9999999999999999999999999999999999

N,M,X = get_nums_l()

# 全てのアルゴリズムがX以上のとき、その時の最小金額を入れる
# 全てのアルゴリズムがX未満のとき、INFを入れる
dp = [INF] * (1 << M)
# 全てのアルゴリズムがX以上のときは0円で買える
dp[(1 << M) - 1] = 0

for n in range(N):
    A = get_nums_l()
    # この本でどのアルゴリズムの学習力が上がるか
    s = 0
    for i in range(1, M+1):
        if A[i] >= X:
            s += 1 << (i-1)

    # 全てのアルゴリズムがX以上になる状態から、本を買うことでX未満になる状態の最小金額を更新する
    for j in range(1 << M):
        if dp[j] != INF:
            dp[j|s] = min(dp[j|s], dp[j] + A[0])

if dp[(1 << M) - 1] == INF:
    print(-1)
else:
    print(dp[(1 << M) -1])
