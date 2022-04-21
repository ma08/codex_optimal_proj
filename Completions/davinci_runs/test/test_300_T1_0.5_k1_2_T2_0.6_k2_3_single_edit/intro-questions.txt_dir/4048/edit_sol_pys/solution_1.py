

import math

n = int(input())

if n == 1:
    print(1)
    exit()

moves = 1

while n > 1:
    if n % 2 == 0:
        n = n // 2
        moves += 1
    else:
        n += 1

print(moves)
