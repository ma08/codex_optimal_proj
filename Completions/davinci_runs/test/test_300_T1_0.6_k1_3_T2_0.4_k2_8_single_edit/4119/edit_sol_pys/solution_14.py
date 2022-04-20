

import sys


def min_moves(pieces, target_coordinates):
    target_coordinates.sort()
    moves_required = 0

    for i in range(len(target_coordinates)):
        moves_required += abs(pieces[i] - target_coordinates[i])

    return moves_required


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())  # read the number of pieces and the number of target coordinates
    x = list(map(int, sys.stdin.readline().split()))  # read the pieces

    print(min_moves(x, x))
