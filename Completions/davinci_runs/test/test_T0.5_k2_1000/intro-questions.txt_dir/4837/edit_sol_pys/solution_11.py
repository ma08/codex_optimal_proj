
import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = []
for i in range(height):
    line = str(input())  # width characters, each either 0 or .
    grid.append(line)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# Three coordinates: a node, its right neighbor, its bottom neighbor
for i in range(height):
    for j in range(width):
        if grid[i][j] == '0':
            print(str(j) + ' ' + str(i) + ' ', end='')
            if j < width - 1:
                for k in range(j + 1, width):
                    if grid[i][k] == '0':
                        print(str(k) + ' ' + str(i) + ' ', end='')
                        break
            else:
                print('-1 -1 ', end='')
            if i < height - 1:
                for k in range(i + 1, height):
                    if grid[k][j] == '0':
                        print(str(j) + ' ' + str(k))
                        break
            else:
                print('-1 -1')
            break

# Three coordinates: a node, its right neighbor, its bottom neighbor
# print('0 0 1 0 0 1')
# print('0 0 0 0 1 0')
# print('0 0 0 0 0 0')
# print('0 0 0 0 0 0')
# print('0 0 0 0 0 0')
# print('0 0 0 0 0 0')
