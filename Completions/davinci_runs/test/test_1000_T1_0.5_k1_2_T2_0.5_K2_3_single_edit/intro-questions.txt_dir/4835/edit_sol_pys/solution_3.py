
import sys

def main():
    line = sys.stdin.readline()
    line = line.split()
    t = int(line[0])
    N = int(line[1])
    M = int(line[2])
    grid = []
    # print(t, N, M)
    for i in range(N):
        line = sys.stdin.readline()
        line = line.strip()
        grid.append(line)
        # print(line)

    # find the starting position
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start_i = i
                start_j = j
                break

    # print(start_i, start_j)
    # initializing the distance from starting position to all other positions
    dist = [[-1 for i in range(M)] for j in range(N)]
    dist[start_i][start_j] = 0

    # BFS
    queue = []
    queue.append((start_i, start_j))
    while len(queue) > 0:
        i, j = queue.pop(0)
        # print(i, j)
        # check up
        if i > 0:
            if grid[i-1][j] == '0' or grid[i-1][j] == 'S':
                if dist[i-1][j] == -1:
                    queue.append((i-1, j))
                    dist[i-1][j] = dist[i][j] + 1
            elif grid[i-1][j] == 'U':
                if dist[i-1][j] == -1:
                    queue.append((i-1, j))
                    dist[i-1][j] = dist[i][j] + 1
        # check down
        if i < N-1:
            if grid[i+1][j] == '0' or grid[i+1][j] == 'S':
                if dist[i+1][j] == -1:
                    queue.append((i+1, j))
                    dist[i+1][j] = dist[i][j] + 1
            elif grid[i+1][j] == 'D':
                if dist[i+1][j] == -1:
                    queue.append((i+1, j))
                    dist[i+1][j] = dist[i][j] + 1
        # check left
        if j > 0:
            if grid[i][j-1] == '0' or grid[i][j-1] == 'S':
                if dist[i][j-1] == -1:
                    queue.append((i, j-1))
                    dist[i][j-1] = dist[i][j] + 1
            elif grid[i][j-1] == 'L':
                if dist[i][j-1] == -1:
                    queue.append((i, j-1))
                    dist[i][j-1] = dist[i][j] + 1
        # check right
        if j < M-1:
            if grid[i][j+1] == '0' or grid[i][j+1] == 'S':
                if dist[i][j+1] == -1:
                    queue.append((i, j+1))
                    dist[i][j+1] = dist[i][j] + 1
            elif grid[i][j+1] == 'R':
                if dist[i][j+1] == -1:
                    queue.append((i, j+1))
                    dist[i][j+1] = dist[i][j] + 1
        # print(queue)
        # print(dist)

    # print(dist)

    # check if reached the border
    if dist[0][0] != -1 and dist[0][0] <= t:
        print(dist[0][0])
    elif dist[0][M-1] != -1 and dist[0][M-1] <= t:
        print(dist[0][M-1])
    elif dist[N-1][0] != -1 and dist[N-1][0] <= t:
        print(dist[N-1][0])
    elif dist[N-1][M-1] != -1 and dist[N-1][M-1] <= t:
        print(dist[N-1][M-1])
    else:
        print('NOT POSSIBLE')


if __name__ == '__main__':
    main()
