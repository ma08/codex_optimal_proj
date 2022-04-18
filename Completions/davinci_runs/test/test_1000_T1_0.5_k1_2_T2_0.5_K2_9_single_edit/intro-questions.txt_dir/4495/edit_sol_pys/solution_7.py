
import math

a, b, x = map(int, input().split())

if a % x == 0:
    print(math.floor(b / x) - math.floor(a / x) + 1)
else:
    print(math.floor(b / x) - math.floor(a / x))
