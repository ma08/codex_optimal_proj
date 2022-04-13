
import sys

def main():
    # Get the input
    N = int(sys.stdin.readline())
    grid = []
    for i in range(N):
        grid.append(sys.stdin.readline().strip())

    # Find the spies and safehouses
    spies = []
    safehouses = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'S':
                spies.append((i, j))
            elif grid[i][j] == 'H':
                safehouses.append((i, j))

    # Find the max distance
    max_distance = 0
    for spy in spies:
        min_distance = N * N
        for safehouse in safehouses:
            distance = abs(spy[0] - safehouse[0]) + abs(spy[1] - safehouse[1])
            if distance < min_distance:
                min_distance = distance
        if min_distance > max_distance:
            max_distance = min_distance
    print(max_distance)


if __name__ == "__main__":
    main()
