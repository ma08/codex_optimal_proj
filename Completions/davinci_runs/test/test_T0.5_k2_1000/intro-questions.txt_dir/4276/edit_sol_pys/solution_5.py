import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())

field = [list(input()) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        if field[i][j] == '#':
            continue
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if field[nx][ny] == '#':
                count += 1
        field[i][j] = count

for i in range(H):
    print(''.join(map(str, field[i])))
