
import sys

def read_input():
    return sys.stdin.readline()

def write_output(msg):
    sys.stdout.write(msg + '\n')

def main():
    t, N, M = map(int, read_input().split())
    grid = [read_input().strip() for _ in range(N)]

    # find starting point
    s_row, s_col = None, None
    for row in range(N):
        for col in range(M):
            if grid[row][col] == 'S':
                s_row, s_col = row, col
                break

    # find possible paths from a given point
    def find_paths(row, col, t):
        paths = []
        if row >= 1 and (grid[row-1][col] == '.' or grid[row-1][col] == 'S' or grid[row-1][col] == 'U'):
            paths.append((row-1, col, t+1))
        if row < N-1 and (grid[row+1][col] == '.' or grid[row+1][col] == 'S' or grid[row+1][col] == 'D'):
            paths.append((row+1, col, t+1))
        if col >= 1 and (grid[row][col-1] == '.' or grid[row][col-1] == 'S' or grid[row][col-1] == 'L'):
            paths.append((row, col-1, t+1))
        if col < M-1 and (grid[row][col+1] == '.' or grid[row][col+1] == 'S' or grid[row][col+1] == 'R'):
            paths.append((row, col+1, t+1))
        return paths

    # BFS to find the min time
    def bfs(row, col, t):
        visited = set()
        q = []
        q.append((row, col, t))
        visited.add((row, col))
        while q:
            cur_row, cur_col, cur_t = q.pop(0)
            if cur_t > t or cur_row < 0 or cur_row >= N or cur_col < 0 or cur_col >= M:
                continue
            if cur_row == 0 or cur_row == N-1 or cur_col == 0 or cur_col == M-1:
                return cur_t
            paths = find_paths(cur_row, cur_col, cur_t)
            for path in paths:
                row, col, t = path
                if path not in visited:
                    q.append(path)
                    visited.add((row, col))
        return -1

    result = bfs(s_row, s_col, 0)
    if result == -1:
        write_output('NOT POSSIBLE')
    else:
        write_output(str(result))

if __name__ == '__main__':
    main()
