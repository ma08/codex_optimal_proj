
from collections import deque


def find_nearest_safe_house(matrix, start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y, 0))
    safe_house = []
    matrix[start_x][start_y] = 0
    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                if matrix[new_x][new_y] == 'S':
                    safe_house.append(dist + 1)
                elif matrix[new_x][new_y] == '.':
                    matrix[new_x][new_y] = dist + 1
                    queue.append((new_x, new_y, dist + 1))

def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    max_dist = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'S':
                safe_house = find_nearest_safe_house(matrix, i, j)
                max_dist = max(max_dist, max(safe_house))
    print(max_dist)

if __name__ == '__main__':
    main()
