

# 入力した数値のうち大きい方を1回押す
a, b = map(int, input().split()) # 入力
print(a + b - max(a, b)) # 計算

# 入力された数値のうち大きい方を1回押す
print(a + b - max(a, b))
