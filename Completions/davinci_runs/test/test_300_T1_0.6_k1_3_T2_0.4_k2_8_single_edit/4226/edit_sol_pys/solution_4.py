
import math

x, y = map(int, input().split())

if y % 2 == 0 and math.ceil(y / 2) >= x:
    print("Yes")
else:
    print("No")
