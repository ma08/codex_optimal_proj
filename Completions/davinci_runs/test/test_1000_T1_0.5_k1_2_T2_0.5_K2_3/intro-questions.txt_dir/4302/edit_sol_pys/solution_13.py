

# 入力
a, b = map(int, input().split())

# 入力された数値のうち大きい方を1回押して、合計を出力
print(a + b - max(a, b))
