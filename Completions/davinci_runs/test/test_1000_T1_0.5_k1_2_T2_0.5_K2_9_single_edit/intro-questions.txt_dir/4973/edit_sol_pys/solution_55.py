

#!/bin/python3

import os
import sys

def knightlOnAChessboard(n, a, b):
    moves = [[a, b], [a, -b], [b, a], [b, -a], [-a, b], [-a, -b], [-b, a], [-b, -a]]
    board = [[0] * n for j in range(n)]
    board[0][0] = 1
    q = [[0, 0]]
    while len(q) > 0:
        x, y = q.pop(0)
        for move in moves:
            newx = x + move[0]
            newy = y + move[1]
            if newx >= 0 and newx < n and newy >= 0 and newy < n and board[newx][newy] == 0:
                board[newx][newy] = board[x][y] + 1
                q.append([newx, newy])
    return board[-1][-1]

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    result = [[knightlOnAChessboard(n, a, b) for a in range(1, n)] for b in range(1, n)]

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
