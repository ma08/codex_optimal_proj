
import sys

def main():
    n = int(sys.stdin.readline())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    spy = None
    safehouses = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                spy = (i, j)
            elif grid[i][j] == 'H':
                safehouses.append((i, j))

    distances = []
    for house in safehouses:
        distances.append(abs(spy[0] - house[0]) + abs(spy[1] - house[1]))
    print(max(distances))

if __name__ == "__main__":
    main()
