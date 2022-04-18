from collections import deque

def isSafe(board, visited, i, j):
    return i >= 0 and i < len(board) and j >= 0 and j < len(board) and board[i][j] != '#' and not visited[i][j]

def min_steps(board):
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    q = deque()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'K':
                q.append((i, j, 0))
                visited[i][j] = True

    while q.qsize() > 0:
        x, y, steps = q.popleft()
        if x == 0 and y == 0:
            return steps

        if isSafe(board, visited, x + 2, y + 1):
            q.append((x + 2, y + 1, steps + 1))
            visited[x + 2][y + 1] = True

        if isSafe(board, visited, x + 2, y - 1):
            q.append((x + 2, y - 1, steps + 1))
            visited[x + 2][y - 1] = True

        if isSafe(board, visited, x - 2, y + 1):
            q.append((x - 2, y + 1, steps + 1))
            visited[x - 2][y + 1] = True

        if isSafe(board, visited, x - 2, y - 1):
            q.append((x - 2, y - 1, steps + 1))
            visited[x - 2][y - 1] = True

        if isSafe(board, visited, x + 1, y + 2):
            q.append((x + 1, y + 2, steps + 1))
            visited[x + 1][y + 2] = True

        if isSafe(board, visited, x + 1, y - 2):
            q.append((x + 1, y - 2, steps + 1))
            visited[x + 1][y - 2] = True

        if isSafe(board, visited, x - 1, y + 2):
            q.append((x - 1, y + 2, steps + 1))
            visited[x - 1][y + 2] = True

        if isSafe(board, visited, x - 1, y - 2):
            q.append((x - 1, y - 2, steps + 1))
            visited[x - 1][y - 2] = True

    return -1

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))
print(min_steps(board))
