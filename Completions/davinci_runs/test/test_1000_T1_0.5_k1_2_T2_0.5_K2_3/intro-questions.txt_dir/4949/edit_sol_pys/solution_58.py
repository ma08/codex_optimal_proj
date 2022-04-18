# https://open.kattis.com/problems/cudoviste


def is_safe(x, y, grid):
    if x < 0 or x >= W or y < 0 or y >= H:
        return False
    return grid[x][y] == '.'


def count_cars(x, y, grid):
    count = 0
    if not is_safe(x, y, grid):
        return count
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not is_safe(x + i, y + j, grid):
                count += 1
    return count


N, W, H = map(int, input().split())

grid = []
for _ in range(H):
    grid.append(list(input()))

count = [0] * 5
for i in range(W):
    for j in range(H):
        count[count_cars(i, j, grid)] += 1

for i in range(N): print(count[i])
