

import math

n = int(input()) # input the number

if n == 1:
    print(0) # if the number is 1, print 0
    exit()

moves = 0 # start the variable

while n > 1:
    moves += 1
    if n % 2 == 0:
        n = n // 2
    else:
        n += 1

print(moves)
