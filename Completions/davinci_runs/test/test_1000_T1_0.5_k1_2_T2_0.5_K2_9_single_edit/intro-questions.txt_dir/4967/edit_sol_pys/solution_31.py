

def main():
    n = int(input())
    grid = []
    for i in range(n):
        line = input()
        grid.append(list(line))
    # print(grid)
    max_distance = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                # print(i, j)
                distance = find_distance(i, j, grid)
                # print(distance)
                if distance > max_distance:
                    max_distance = distance
    print(max_distance)

def find_distance(i, j, grid):
    distance = 0
    n = len(grid)
    for k in range(n):
        for l in range(n):
            if grid[k][l] == 'H':
                distance = max(distance, abs(k-i) + abs(l-j))
    return distance

if __name__ == "__main__":
    main()
