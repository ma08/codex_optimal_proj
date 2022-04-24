

# a = 10, b = 7, x = 100, k = 2
a, b, x, k = map(int, input().split())

# 値が大きい数を求める
max_value = (x - b * k) // a

# 1桁目が9になっている場合、1減らして終了
if max_value // 10**(k - 1) == 9:
    max_value -= 1

# 数値が0以下の場合
if max_value <= 0:
    print(0)
    exit()

# 値が小さい数を求める
min_value = 10**(k - 1)

print(max_value - min_value + 1)
