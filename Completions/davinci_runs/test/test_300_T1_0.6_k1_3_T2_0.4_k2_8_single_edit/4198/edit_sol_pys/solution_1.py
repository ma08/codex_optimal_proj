

import math

input_data = input().split(' ')
a = int(input_data[0])
b = int(input_data[1])
x = int(input_data[2])

if a == 1:
    print(x)
else:
    y = (x-b)/a
    print(int(math.floor(y)))
