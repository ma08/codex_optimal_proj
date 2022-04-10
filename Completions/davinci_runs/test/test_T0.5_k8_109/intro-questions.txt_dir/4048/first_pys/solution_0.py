

import sys

n = int(sys.stdin.readline())

def min_moves(n):
    moves = 0
    i = 1
    j = 1
    while True:
        if n == i:
            return moves + 1
        elif n == j:
            return moves + 1
        elif n < i:
            if n > j:
                return moves + n - j
            else:
                return moves + i - n
        else:
            moves += 1
            i += 1
            j += 1

print(min_moves(n))