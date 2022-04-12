import sys

def main():
    n, m = [int(i) for i in input().split()]
    grid = []
    for i in range(n):
        grid.append(input().strip())
    count = 0
    for i in range(n):
        if grid[i][0] == '_':
            count += 1
            while i < n and grid[i][0] == '_':
                i += 1
    print(count)

main()
