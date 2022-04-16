

# 入力
a, b = map(int, input().split())

# 入力された数値のうち大きい方を2回押すと
print(a + b - max(a, b))
