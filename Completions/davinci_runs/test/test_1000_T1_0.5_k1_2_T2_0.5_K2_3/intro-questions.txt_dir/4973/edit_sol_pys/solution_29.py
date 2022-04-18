import sys

def bfs(board, n, x, y):
    queue = []
    queue.append((x, y, 0))
    while queue:
        i, j, steps = queue.pop(0)
        if board[i][j] == 'K':
            return steps
        if board[i][j] == '.':
            board[i][j] = '#'
            if i + 2 < n and j + 1 < n and board[i + 2][j + 1] != '#':
                queue.append((i + 2, j + 1, steps + 1))
            if i + 2 < n and j - 1 >= 0 and board[i + 2][j - 1] != '#':
                queue.append((i + 2, j - 1, steps + 1))
            if i - 2 >= 0 and j + 1 < n and board[i - 2][j + 1] != '#':
                queue.append((i - 2, j + 1, steps + 1))
            if i - 2 >= 0 and j - 1 >= 0 and board[i - 2][j - 1] != '#':
                queue.append((i - 2, j - 1, steps + 1))
            if i + 1 < n and j + 2 < n and board[i + 1][j + 2] != '#':
                queue.append((i + 1, j + 2, steps + 1))
            if i + 1 < n and j - 2 >= 0 and board[i + 1][j - 2] != '#':
                queue.append((i + 1, j - 2, steps + 1))
            if i - 1 >= 0 and j + 2 < n and board[i - 1][j + 2] != '#':
                queue.append((i - 1, j + 2, steps + 1))
            if i - 1 >= 0 and j - 2 >= 0 and board[i - 1][j - 2] != '#':
                queue.append((i - 1, j - 2, steps + 1))
    return -1

def main():
    n = int(sys.stdin.readline()) 
    board = []
    for i in range(n):
        board.append(sys.stdin.readline().strip())
    print(bfs(board, n, 1, 1))

if __name__ == '__main__':
    main()
