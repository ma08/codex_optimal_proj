

# 入力
a, b, c = map(int, input().split())

# 入力された数値のうち大きい方を2回押すことで、小さい方を求める。
# これを3回繰り返すことで、中央値を求めることができる。
print(a + b + c - max(a, b, c) - min(a, b, c))
