

def get_min_dist(n, k, matrix, start_x, start_y, end_x, end_y, visited):
    if start_x == end_x and start_y == end_y:
        return 0
    if start_x < 0 or start_x >= n or start_y < 0 or start_y >= n:
        return float('inf')
    if matrix[start_x][start_y] == 1:
        return float('inf')
    if visited[start_x][start_y] == 1:
        return float('inf')
    visited[start_x][start_y] = 1
    min_dist = float('inf')
    for i in range(k):
        min_dist = min(min_dist, 1 + get_min_dist(n, k, matrix, start_x + i, start_y, end_x, end_y, visited))
        min_dist = min(min_dist, 1 + get_min_dist(n, k, matrix, start_x - i, start_y, end_x, end_y, visited))
        min_dist = min(min_dist, 1 + get_min_dist(n, k, matrix, start_x, start_y + i, end_x, end_y, visited))
        min_dist = min(min_dist, 1 + get_min_dist(n, k, matrix, start_x, start_y - i, end_x, end_y, visited))
    visited[start_x][start_y] = 0
    return min_dist

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().split()])
    start_x, start_y, end_x, end_y = [int(x) for x in input().split()]
    visited = [[0 for i in range(n)] for j in range(n)]
    print(get_min_dist(n, k, matrix, start_x, start_y, end_x, end_y, visited))
