
import math

def find(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    b = (math.sqrt(4 * n - 7) + 1) / 2
    if b % 1 == 0:
        return b
    else:
        return int(math.ceil(b))

print(find(int(input())))
