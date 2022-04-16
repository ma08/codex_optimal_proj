
import sys
import math

def euclidean(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

def manhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def get_neighbors(coord, n):
    x,y = coord
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < n-1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < n-1:
        neighbors.append((x, y+1))
    return neighbors

def get_next_coord(coord, n, board):
    x,y = coord
    neighbors = get_neighbors(coord, n)
    for neighbor in neighbors:
        if board[neighbor[0]][neighbor[1]] == board[x][y] + 1:
            return neighbor
    return None

def find_path(coord, n, board):
    path = [coord]
    next_coord = get_next_coord(coord, n, board)
    while next_coord:
        path.append(next_coord)
        next_coord = get_next_coord(next_coord, n, board)
    return path

def find_paths(n, k, board):
    paths = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                paths.append(find_path((i, j), n, board))
    return paths

def get_length(path):
    length = 0
    for i in range(len(path)-1):
        length += manhattan(path[i][0], path[i][1], path[i+1][0], path[i+1][1])
    return length

def get_shortest_path(paths):
    shortest_length = sys.maxsize
    shortest_path = None
    for path in paths:
        if len(path) == k:
            length = get_length(path)
            if length < shortest_length:
                shortest_length = length
                shortest_path = path
    return shortest_path

def main():
    n, k = [int(x) for x in input().split()]
    board = []
    for i in range(n):
        board.append([int(x) for x in input().split()])
    paths = find_paths(n, k, board)
    shortest_path = get_shortest_path(paths)
    if shortest_path:
        print(get_length(shortest_path))
    else:
        print(-1)

if __name__ == '__main__':
    main()
