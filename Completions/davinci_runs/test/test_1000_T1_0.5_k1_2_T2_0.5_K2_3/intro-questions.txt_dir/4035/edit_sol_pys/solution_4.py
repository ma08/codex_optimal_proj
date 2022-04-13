
import math
a, b = map(int, input().split())

for i in range(1, a+1):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:  # 条件分岐
        print(i)
        exit()
print(-1)
