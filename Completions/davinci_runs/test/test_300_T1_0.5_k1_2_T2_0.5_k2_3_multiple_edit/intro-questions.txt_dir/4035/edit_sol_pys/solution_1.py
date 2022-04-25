
import math

a, b = map(float, input().split())

if math.floor(b * 0.08) == a and math.floor(b * 0.1) == b:
    print(b)
else:
    print(-1)
