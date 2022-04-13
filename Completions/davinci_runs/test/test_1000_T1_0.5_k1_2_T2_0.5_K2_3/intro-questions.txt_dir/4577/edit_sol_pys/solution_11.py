
a, b, c = map(int, input().split())  # 3つの整数を入力
if a <= c <= b:  # aとbの間にcがあるか判定
    print('Yes')
else:
    print('No')
