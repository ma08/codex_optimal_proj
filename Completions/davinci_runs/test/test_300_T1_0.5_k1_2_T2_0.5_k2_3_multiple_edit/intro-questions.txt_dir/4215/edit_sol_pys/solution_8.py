#-----Main-----


import math

a, b = map(int, input().split())

if a == 1:
    print(1)
else:
    print(math.ceil(math.log(b, a)) + 1)
