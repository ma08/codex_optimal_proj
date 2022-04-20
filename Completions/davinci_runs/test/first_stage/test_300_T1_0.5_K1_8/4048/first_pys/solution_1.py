

import sys

num = int(sys.stdin.readline())

def min_moves(num):
    moves = 0

    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        moves += 1
    return moves

print(min_moves(num))