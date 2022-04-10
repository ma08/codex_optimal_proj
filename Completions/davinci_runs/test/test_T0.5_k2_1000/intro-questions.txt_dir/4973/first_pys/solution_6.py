

import sys
from collections import deque

# read the input
N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline().strip()))

# find the starting point of the knight
for i in range(N):
    for j in range(N):
        if board[i][j] == "K":
            start = (i, j)
            break

# define the valid moves
moves = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
]

# define a function to check if a move is valid
def valid_move(move):
    if 0 <= move[0] < N and 0 <= move[1] < N and board[move[0]][move[1]] != "#":
        return True
    return False

# define a function to get all valid moves from a cell
def get_valid_moves(cell):
    valid_moves = []
    for move in moves:
        if valid_move((cell[0] + move[0], cell[1] + move[1])):
            valid_moves.append((cell[0] + move[0], cell[1] + move[1]))
    return valid_moves

# define a function to find the minimum steps
def min_steps(start):
    # create a queue to store the cells to be visited
    queue = deque()
    queue.append((start, 0))

    # create a set to store the cells visited
    visited = set()
    visited.add(start)

    # use BFS to find the minimum steps
    while queue:
        cell, steps = queue.popleft()
        if cell == (0, 0):
            return steps
        for move in get_valid_moves(cell):
            if move not in visited:
                visited.add(move)
                queue.append((move, steps + 1))

    return -1

print(min_steps(start))