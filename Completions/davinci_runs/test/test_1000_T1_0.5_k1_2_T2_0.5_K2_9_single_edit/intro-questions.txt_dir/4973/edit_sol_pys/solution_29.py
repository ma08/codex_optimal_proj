
def isValid(r, c):
    if r >= 0 and r < n and c >= 0 and c < n:
        return True

    return False

def bfs(r, c):
    global ans
    queue = [(r, c, 0)]
    visited = set()
    while queue:
        r, c, moves = queue.pop(0)
        if r == 0 and c == 0:
            ans = moves
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

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))

ans = -1
for i in range(n):
    for j in range(n):
        if board[i][j] == 'K':
            bfs(i, j)

print(ans)
