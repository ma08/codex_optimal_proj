import math

a, b = map(int, input().split())
if a > 9 or b > 9:
    print(-1)
else:
    print(math.floor(a * b))
