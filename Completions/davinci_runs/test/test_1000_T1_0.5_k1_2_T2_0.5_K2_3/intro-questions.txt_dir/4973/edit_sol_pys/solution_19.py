
# Solution 1 
def get_moves(r, c):
    return [(r + 2, c + 1), (r + 2, c - 1), (r - 2, c + 1), (r - 2, c - 1), (r + 1, c + 2), (r + 1, c - 2), (r - 1, c + 2), (r - 1, c - 2)]

def is_valid(r, c):
    return r >= 1 and c >= 1 and r <= n and c <= n

def is_knight(r, c):
    return board[r - 1][c - 1] == 'K'

def is_empty(r, c):
    return board[r - 1][c - 1] == '.'

def is_blocked(r, c):
    return board[r - 1][c - 1] == '#'

def bfs(r, c):
    q = [(r, c, 0)]
    while q:
        r, c, d = q.pop(0)
        if r == c == 1:
            return d
        for r1, c1 in get_moves(r, c):
            if is_valid(r1, c1) and is_empty(r1, c1) and (r1, c1) not in vis:
                vis.add((r1, c1))
                q.append((r1, c1, d + 1))
    return -1

n = int(input())
board = []
for _ in range(n):
    board.append(input())
vis = set()
for i in range(n):
    for j in range(n):
        if is_knight(i + 1, j + 1):
            print(bfs(i + 1, j + 1))
            break
