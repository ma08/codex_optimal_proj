import math
a, b = map(int, input().split())
num = int(str(a) + str(b))
if math.sqrt(num).is_integer():
    print("Yes")
else:
    print("No")
