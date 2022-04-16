
import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    grid = []
    for i in range(n):
        grid.append(sys.stdin.readline().strip())
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '_':
                count += 1
                while j < m and grid[i][j] == '_':
                    j += 1
    print(count)

main()
