# import sys
#
# def main():
#     N, M = [int(x) for x in sys.stdin.readline().strip().split()]
#     grid = []
#     for i in range(N):
#         grid.append([x for x in sys.stdin.readline().strip()])
#     for i in range(N):
#         for j in range(M):
#             if grid[i][j] == 'V':
#                 grid[i][j] = '.'
#                 if i < N - 1 and grid[i + 1][j] == '.':
#                     grid[i + 1][j] = 'V'
#                 if j > 0 and j < M - 1 and grid[i][j - 1] == '.' and grid[i][j + 1] == '.':
#                     grid[i][j - 1] = 'V'
#                     grid[i][j + 1] = 'V'
#     for i in range(N):
#         print("".join(grid[i]))
#
# main()

from collections import deque
import sys

def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    grid = [[] for _ in range(N)]
    queue = deque()
    for i in range(N):
        grid[i] = [x for x in sys.stdin.readline().strip()]
        for j in range(M):
            if grid[i][j] == 'V':
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        grid[x][y] = '.'
        if x < N - 1 and grid[x + 1][y] == '.':
            grid[x + 1][y] = 'V'
            queue.append((x + 1, y))
        if y > 0 and y < M - 1 and grid[x][y - 1] == '.' and grid[x][y + 1] == '.':
            grid[x][y - 1] = 'V'
            grid[x][y + 1] = 'V'
            queue.append((x, y - 1))
            queue.append((x, y + 1))
    for i in range(N):
        print("".join(grid[i]))

main()
