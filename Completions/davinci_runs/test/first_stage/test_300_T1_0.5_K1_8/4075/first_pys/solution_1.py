

import sys

N, M = map(int, sys.stdin.readline().split())

# 各電球に影響を与えるスイッチのリスト
# bulbs[i][j] = i番目の電球に影響を与えるj番目のスイッチ
bulbs = []
for i in range(M):
    bulbs.append(list(map(int, sys.stdin.readline().split()))[1:])

# 各電球のON/OFF
# on_off[i] = i番目の電球がONかどうか
on_off = list(map(int, sys.stdin.readline().split()))

# 全ての電球をONにするスイッチの状態の組み合わせ数
count = 0

# 全てのスイッチの状態の組み合わせをbit全探索
for i in range(2**N):
    # 全ての電球がONになっているか
    all_on = True
    for j in range(M):
        # j番目の電球に影響を与えるスイッチの数
        k = len(bulbs[j])
        # j番目の電球に影響を与えるスイッチのONの数
        on_num = 0
        for l in range(k):
            if i & (1 << (bulbs[j][l] - 1)) != 0:
                on_num += 1
        # j番目の電球がONになっているか
        bulb_on = (on_num % 2) == on_off[j]
        if not bulb_on:
            all_on = False
            break
    if all_on:
        count += 1
print(count)