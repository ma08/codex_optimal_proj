
def isValid(r, c):
    if r >= 0 and r < N and c >= 0 and c < N:
        return True
    return False

def bfs(r, c):
    queue = [(r, c, 0)]
    visited = set()
    while queue:
        r, c, moves = queue.pop(0)
        if r == 0 and c == 0:
            print(moves)
            return
        if (r, c) not in visited:
            visited.add((r, c))
            for i in range(8):
                new_r = r + dr[i]
                new_c = c + dc[i]
                if isValid(new_r, new_c) and board[new_r][new_c] == '.':
                    queue.append((new_r, new_c, moves + 1))

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

for i in range(N):
    for j in range(N):
        if board[i][j] == 'K':
            bfs(i, j)
