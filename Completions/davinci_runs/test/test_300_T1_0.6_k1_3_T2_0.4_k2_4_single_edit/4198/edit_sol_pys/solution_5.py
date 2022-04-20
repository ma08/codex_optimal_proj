
import math

input_line = input().split(' ')
a = int(input_line[0])
b = int(input_line[1])
x = int(input_line[2])

if a == 1:
    print(x)
else:
    y = (x-b)/a
    print(int(math.floor(y)))
