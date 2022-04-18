
import math
import sys


def min_moves(pieces, target_coordinates):
    target_coordinates.sort() # sort the target coordinates
    moves_required = 0 # initialize moves required

    for i in range(len(target_coordinates)):
        moves_required += abs(pieces[i] - target_coordinates[i]) # calculate the moves required

    return moves_required # return the moves required


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split()) # read the input
    x = list(map(int, sys.stdin.readline().split())) # read the input

    print(min_moves(x, x)) # print the minimum moves
