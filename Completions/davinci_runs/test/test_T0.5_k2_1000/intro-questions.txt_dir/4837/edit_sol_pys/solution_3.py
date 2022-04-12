
import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(line)

def get_neighbors(grid, x, y):
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < len(grid[0]) - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < len(grid) - 1:
        neighbors.append((x, y+1))
    return neighbors

def main():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '0':
                print(x, y, end=' ')
                neighbors = get_neighbors(grid, x, y)
                for neighbor in neighbors:
                    if grid[neighbor[1]][neighbor[0]] == '0':
                        print(neighbor[0], neighbor[1], end=' ')
                    else:
                        print(-1, -1, end=' ')
                print()

if __name__ == "__main__":
    main()
