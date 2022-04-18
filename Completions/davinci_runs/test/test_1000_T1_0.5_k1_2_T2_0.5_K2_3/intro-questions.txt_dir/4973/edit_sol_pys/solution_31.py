#!/bin/python3

import os
import sys

#
# Complete the knightOnAChessboard function below.
#
def knightOnAChessboard(n):
    res = [[0 for i in range(n-1)] for j in range(n-1)]
    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                continue
            board = [[0 for k in range(n)] for l in range(n)]
            moves = [[i, j], [i, -j], [j, i], [j, -i], [-i, j], [-i, -j], [-j, i], [-j, -i]]
            board[0][0] = 1
            q = []
            q.append([0, 0])
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
            if board[n-1][n-1] == 0:
                res[i-1][j-1] = -1
            else:
                res[i-1][j-1] = board[n-1][n-1] - 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
