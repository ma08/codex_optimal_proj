
import math

input = input().split()
a = int(input[0]) #a
b = int(input[1]) #b
x = int(input[2]) #x

if a == 1:
    print(x)
else:
    y = (x-b)/a
    print(int(math.floor(y)))
