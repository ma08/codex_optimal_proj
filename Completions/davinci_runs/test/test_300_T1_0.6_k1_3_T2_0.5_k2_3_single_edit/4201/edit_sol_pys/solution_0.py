

def get_input():
    """ Gets the input from the user. """
    H, W, K = map(int, input().split())
    H, W, K = int(H), int(W), int(K)
    return H, W, K

def get_grid(H, W):
    """ Gets the grid from the user. """
    grid = []
    for i in range(H):
        grid.append(input())
    return grid

def count_black(grid, H, W, rows, columns):
    """ Counts the number of black squares in the grid after painting the rows and columns red. """
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#" and i not in rows and j not in columns:
                count += 1
    return count

def count_choices(grid, H, W, K):
    """ Counts the number of choices that satisfy the condition. """
    count = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            rows = []
            for k in range(H):
                if i >> k & 1:
                    rows.append(k)
            columns = []
            for k in range(W):
                if j >> k & 1:
                    columns.append(k)
            if count_black(grid, H, W, rows, columns) == K:
                count += 1
    return count

def main():
    """ The main function. """
    H, W, K = get_input()
    grid = get_grid(H, W)
    choices = count_choices(grid, H, W, K)
    print(choices)

if __name__ == "__main__":
    main()
