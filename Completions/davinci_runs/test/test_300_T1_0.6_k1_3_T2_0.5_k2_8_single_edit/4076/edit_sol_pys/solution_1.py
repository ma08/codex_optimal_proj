import math

# 入力
a, b, h, m = map(int, input().split())

# 度数法
# 時計の針の座標
x_h = a * math.sin(math.radians(30 * h + 0.5 * m))
y_h = a * math.cos(math.radians(30 * h + 0.5 * m))
x_m = b * math.sin(math.radians(6 * m))
y_m = b * math.cos(math.radians(6 * m))

# 座標
x = x_h - x_m
y = y_h - y_m

# 出力
print(math.sqrt(x ** 2 + y ** 2))
