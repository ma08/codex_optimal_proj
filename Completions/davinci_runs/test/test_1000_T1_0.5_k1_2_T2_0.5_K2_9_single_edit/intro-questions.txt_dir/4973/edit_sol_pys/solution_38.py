import queue

def isSafe(board, visited, i, j):
    return i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] != '#' and not visited[i][j]

def min_steps(board):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    q = queue.Queue()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'K':
                q.put((i, j, 0))                
                visited[i][j] = True

    while q.qsize() > 0:
        x, y, steps = q.get()
        if x == 0 and y == 0:
            print(board)
            return steps

        if isSafe(board, visited, x + 2, y + 1):
            q.put((x + 2, y + 1, steps + 1))
            visited[x + 2][y + 1] = True

        if isSafe(board, visited, x + 2, y - 1):
            q.put((x + 2, y - 1, steps + 1))
            visited[x + 2][y - 1] = True

        if isSafe(board, visited, x - 2, y + 1):
            q.put((x - 2, y + 1, steps + 1))
            visited[x - 2][y + 1] = True

        if isSafe(board, visited, x - 2, y - 1):
            q.put((x - 2, y - 1, steps + 1))
            visited[x - 2][y - 1] = True

        if isSafe(board, visited, x + 1, y + 2):
            q.put((x + 1, y + 2, steps + 1))
            visited[x + 1][y + 2] = True

        if isSafe(board, visited, x + 1, y - 2):
            q.put((x + 1, y - 2, steps + 1))
            visited[x + 1][y - 2] = True

        if isSafe(board, visited, x - 1, y + 2):
            q.put((x - 1, y + 2, steps + 1))
            visited[x - 1][y + 2] = True

        if isSafe(board, visited, x - 1, y - 2):
            q.put((x - 1, y - 2, steps + 1))
            visited[x - 1][y - 2] = True

    return -1

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))
print(min_steps(board))
