
x, a, b = map(int, input().split())   # 整数の入力

if abs(x - a) < abs(x - b):           # 左右どちらにあるか
    print('A')                         # 左にある
else:
    print('B')
