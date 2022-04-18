
import sys

def solve(n):
    board = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    def dfs(x,y,board,visited):
        if x < 0 or x >= n or y < 0 or y >= n:
            return 0
        if board[x][y] == 0:
            return 0
        if (x,y) in visited:
            return 0
        visited.add((x,y))

        return 1 + dfs(x+1,y,board,visited) + dfs(x-1,y,board,visited) + dfs(x,y+1,board,visited) + dfs(x,y-1,board,visited)

    visited = set()

    max_val = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and (i,j) not in visited:
                max_val = max(max_val, dfs(i,j,board,visited))

    return max_val

n = int(sys.stdin.readline().strip())
print(solve(n))
