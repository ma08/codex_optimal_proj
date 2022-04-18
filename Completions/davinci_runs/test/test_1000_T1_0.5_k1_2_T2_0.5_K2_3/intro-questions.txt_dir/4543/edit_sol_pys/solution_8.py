
import math

a, b = map(int, input().split())

num = int(str(a) + str(b)) # aとbを結合した数値を作成

if math.sqrt(num).is_integer(): # 小数点以下が0であるかを判定する
    print("Yes")
else:
    print("No")
