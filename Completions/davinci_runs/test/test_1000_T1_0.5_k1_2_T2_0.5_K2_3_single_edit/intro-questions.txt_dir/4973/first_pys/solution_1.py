

#!/bin/python3

import os
import sys

#
# Complete the knightlOnAChessboard function below.
#
def knightlOnAChessboard(n):
    #
    # Write your code here.
    #
    moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
    board = [[0 for i in range(n)] for j in range(n)]
    board[n-1][n-1] = 1
    q = []
    q.append([n-1, n-1])
    while len(q) > 0:
        cur = q.pop(0)
        x = cur[0]
        y = cur[1]
        for move in moves:
            newx = x + move[0]
            newy = y + move[1]
            if newx >= 0 and newx < n and newy >= 0 and newy < n and board[newx][newy] == 0:
                board[newx][newy] = board[x][y] + 1
                q.append([newx, newy])
    return board

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()