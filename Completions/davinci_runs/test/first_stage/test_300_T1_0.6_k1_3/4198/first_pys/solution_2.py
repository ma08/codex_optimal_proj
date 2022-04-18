

import math

input = input().split(' ')
a = int(input[0])
b = int(input[1])
x = int(input[2])

if a == 1:
    print(x)
else:
    y = (x-b)/a
    print(int(math.floor(y)))