

import math

N = int(input())

# アルファベットの個数
alpha_num = 26

# 桁数
digit = int(math.log(N, alpha_num))

# 桁数によって増加する数字の数
digit_num = alpha_num ** (digit - 1)

# 桁数によって増加する数字の数を足して1を引いた値を求める
N -= alpha_num ** digit - digit_num

# 各桁の値を求める
digit_list = []
for i in range(digit):
    # 各桁の値を求める
    digit_list.append(N // digit_num)
    # 次の桁の値を求めるために1桁分減らす
    N -= digit_num
    # 次の桁の値を求めるために桁数を減らす
    digit_num //= alpha_num

# 各桁の値をアルファベットに変換する
result = []
for i in digit_list:
    result.append(chr(97 + i))

print("".join(result))