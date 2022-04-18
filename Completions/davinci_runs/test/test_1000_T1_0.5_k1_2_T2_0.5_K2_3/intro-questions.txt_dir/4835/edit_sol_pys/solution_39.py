

import sys

def read_input():
    return sys.stdin.readline()

def write_output(msg):
    sys.stdout.write(msg + '\n')

def main():
    t, N, M = map(int, read_input().split())
    grid = [read_input().strip() for _ in range(N)]
    # print(t, N, M)
    # print(grid)
    # print()
    # print(grid[0][1])

    # find starting point
    s_row, s_col = None, None
    for row in range(N):
        for col in range(M):
            if grid[row][col] == 'S':
                s_row, s_col = row, col
                # print(s_row, s_col)
                break

    # find possible paths from a given point
    def find_paths(row, col, t):
        paths = []
        if row >= 1 and (grid[row-1][col] == '0' or grid[row-1][col] == 'S' or grid[row-1][col] == 'U') and (row-1, col) not in visited:
            paths.append((row-1, col, t+1))
        if row < N-1 and (grid[row+1][col] == '0' or grid[row+1][col] == 'S' or grid[row+1][col] == 'D') and (row+1, col) not in visited:
            paths.append((row+1, col, t+1))
        if col >= 1 and (grid[row][col-1] == '0' or grid[row][col-1] == 'S' or grid[row][col-1] == 'L') and (row, col-1) not in visited:
            paths.append((row, col-1, t+1))
        if col < M-1 and (grid[row][col+1] == '0' or grid[row][col+1] == 'S' or grid[row][col+1] == 'R') and (row, col+1) not in visited:
            paths.append((row, col+1, t+1))
        return paths

    # print(find_paths(s_row, s_col, 0))

    # BFS to find the shortest path
    def bfs(row, col, t):
        visited = set()
        q = []
        q.append((row, col, t))
        visited.add((row, col, t))
        while q:
            cur_row, cur_col, cur_t = q.pop(0)
            # print(cur_row, cur_col, cur_t)
            if cur_row < 0 or cur_row >= N or cur_col < 0 or cur_col >= M:
                continue
            if cur_row == 0 or cur_row == N-1 or cur_col == 0 or cur_col == M-1:
                return cur_t
            paths = find_paths(cur_row, cur_col, cur_t, visited)
            for path in paths:
                row, col, t = path
                q.append(path)
                visited.add((row, col, t))
        return -1

    result = bfs(s_row, s_col, 0)
    if result == -1:
        write_output('NOT POSSIBLE')
    else:
        write_output(str(result))

if __name__ == '__main__':
    main()
