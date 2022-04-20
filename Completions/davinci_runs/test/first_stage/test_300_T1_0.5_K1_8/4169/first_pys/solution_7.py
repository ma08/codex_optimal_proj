

import sys

N, M = map(int, sys.stdin.readline().split())

# 各店舗で買える最大量と1缶あたりの価格を格納するリスト
# このリストを昇順にソートする
A = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A.append((a, b))
A.sort()

# 各店舗で買える最大量
can_buy = [b for a, b in A]
# 各店舗で買える最大量を累積和をとっておく
for i in range(1, N):
    can_buy[i] += can_buy[i-1]
# 各店舗で買える最大量がMを超える店舗が最初に出てくるindex
index = 0
for i in range(N):
    if can_buy[i] >= M:
        index = i
        break

# 各店舗で1缶あたりの価格
price = [a for a, b in A]

# 各店舗で買える最大量がMを超える店舗はMを超えた分だけ買う
sum_price = M * price[index]
# 各店舗で買える最大量がMを超える店舗より前の店舗は、買える最大量分だけ買う
if index > 0:
    sum_price += sum(price[:index]) * can_buy[index-1]
# 各店舗で買える最大量がMを超える店舗より後ろの店舗は、1缶あたりの価格が最安の店舗で買う
if index < N-1:
    sum_price += sum(price[index+1:]) * (M - can_buy[index])

print(sum_price)