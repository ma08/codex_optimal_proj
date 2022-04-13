

# CODE:
import math

n = int(input())

def calc_side(n):
    side = math.ceil(math.pow(n, 1/3))
    return side

print(calc_side(n))
