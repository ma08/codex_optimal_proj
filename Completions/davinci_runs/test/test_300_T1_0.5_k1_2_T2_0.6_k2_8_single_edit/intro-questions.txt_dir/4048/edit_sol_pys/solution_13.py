
import math

n = int(input())

moves = 0
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

while n > 0:
    moves += 1
    if is_even(n):
        n /= 2
    else:
        n -= 1

print(moves)
