import sys



def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    grid = []
    for i in range(n):
        grid.append(sys.stdin.readline().strip())
    count = 0
    for j in range(m):
        if grid[0][j] == '_':
            count += 1
            while j < m and grid[0][j] == '_':
                j += 1
    print(count)


main()
