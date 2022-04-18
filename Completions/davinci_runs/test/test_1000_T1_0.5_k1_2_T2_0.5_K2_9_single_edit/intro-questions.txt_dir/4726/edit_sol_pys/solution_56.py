

import math

m, n, t = map(int, input().split())  # 入力

if t == 1:
    if n > m:  # 時間が足りない場合
        print("TLE")
    else:
        print("AC")
elif t == 2:
    if 2 ** n > m:  # 時間が足りない場合
        print("TLE")
    else:
        print("AC")
elif t == 3:
    if n ** 4 > m:  # 時間が足りない場合
        print("TLE")
    else:
        print("AC")
elif t == 4:
    if n ** 3 > m:  # 時間が足りない場合
        print("TLE")
    else:
        print("AC")
elif t == 5:
    if n ** 2 > m:  # 時間が足りない場合
        print("TLE")
    else:
        print("AC")
elif t == 6:
    if n * math.log2(n) > m:
        print("TLE")
    else:
        print("AC")
elif t == 7:
    if n > m:
        print("TLE")
    else:
        print("AC")
