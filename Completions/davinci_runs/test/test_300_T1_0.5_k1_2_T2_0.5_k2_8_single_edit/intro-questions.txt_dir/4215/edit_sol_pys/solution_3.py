
import math
#-----main-----

a, b = map(int, input().split())

if a <= b:
    print(0)
else:
    print(math.ceil(a / b) - 1)
