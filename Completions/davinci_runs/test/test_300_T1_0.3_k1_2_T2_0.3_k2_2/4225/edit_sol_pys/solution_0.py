
import sys

a, b, c, k = map(int, sys.stdin.readline().split())  # 標準入力を分割して数値に変換

if k <= a:  # kがa以下の場合
    print(k)
elif k <= a + b:  # kがa+b以下の場合
    print(a)
else:  # それ以外の場合
    print(a - (k - a - b))
