import sys

import math

# input = input().split(' ')
# a = int(input[0])
# b = int(input[1])
# x = int(input[2])

a = int(sys.argv[1])
b = int(sys.argv[2])
x = int(sys.argv[3])

if a == 1:
    print(x)
else:
    y = (x-b)/a
    print(int(math.floor(y)))
