
# 入力
a, b = map(int, input().split())

# 入力された数値のうち大きい方を2回押すことで、小さい方を求める
print(a + b - max(a, b))
