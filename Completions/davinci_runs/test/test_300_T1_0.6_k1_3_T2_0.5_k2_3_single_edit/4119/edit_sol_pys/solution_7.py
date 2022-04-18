
import sys


def min_moves(pieces, target_coordinates):
    moves_required = 0

    for i in range(len(pieces)):
        moves_required += abs(target_coordinates[i] - pieces[i])

    return moves_required
    y = list(map(int, sys.stdin.readline().split()))
    y.sort()


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))

    print(min_moves(x, y))
