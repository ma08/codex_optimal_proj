

# 入力
a, b = map(int, input().split())

# 入力された数値のうち大きい方を2回押す（最大値を2回押すので，その分を引く） #
print(a + b - max(a, b))
