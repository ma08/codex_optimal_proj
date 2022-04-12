
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    grid = [sys.stdin.readline() for _ in range(n)]
    output = [['.' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                continue
            # place shop if no shop in adjacent cells.
            if (i > 0 and output[i-1][j] != 'E') and \
               (i < n-1 and output[i+1][j] != 'E') and \
               (j > 0 and output[i][j-1] != 'E') and \
               (j < m-1 and output[i][j+1] != 'E'):
                output[i][j] = 'E'
    for row in output:
        sys.stdout.write(''.join(row))

if __name__ == '__main__':
    main()
