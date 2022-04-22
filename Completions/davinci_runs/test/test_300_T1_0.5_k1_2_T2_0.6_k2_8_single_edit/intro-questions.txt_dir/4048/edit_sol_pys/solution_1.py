

import math

n = int(input())

def is_power_of_two(n):
    return n != 0 and ((n & (n - 1)) == 0)


def solve(n):
    if n == 1:
        return 0

    moves = 0

    while n > 1:
        moves += 1
        if n % 2 == 0:
            n = n // 2
        else:
            if is_power_of_two(n + 1) and is_power_of_two(n - 1):
                n -= 1
            else:
                n += 1

    return moves


if n == 0:
    print(0)
    exit()

print(solve(n))
