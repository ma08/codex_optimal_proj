# 入力
import math
# ループ
a, b = map(int, input().split())

    # 条件分岐
for i in range(1, a+1):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        print(i)
        exit()
print(-1)
