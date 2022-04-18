
import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    grid = [0] * n
    for i in range(n):
        grid[i] = sys.stdin.readline().strip()
    count = 0
    for j in range(m):
        if grid[0][j] == '*':
            count += 1
            while j < m and grid[0][j] == '*':
                j += 1
    print(count) 

main()
