

import math

a, b = map(float, input().split())

for i in range(1, math.ceil(b / 0.1)+1):
    if math.floor(i * 0.08) == a and math.ceil(i * 0.1) == b:
        print(i)
        exit()
print(-1)
