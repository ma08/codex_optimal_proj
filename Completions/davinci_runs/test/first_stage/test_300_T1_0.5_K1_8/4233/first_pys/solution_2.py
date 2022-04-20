

def main():
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    # print(grid)
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    # print(stars)

    def check(x, y, size):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if grid[x][y] == '.':
            return False
        if size == 1:
            return True
        return check(x, y - 1, size - 1) and check(x, y + 1, size - 1) and check(x - 1, y, size - 1) and check(x + 1, y, size - 1)

    def find_star(x, y):
        for size in range(1, n + m):
            if check(x, y, size):
                return (x, y, size)
        return None

    def solve():
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    star = find_star(i, j)
                    if star is None:
                        print(-1)
                        return
                    grid[i][j] = '.'
                    print(star[0] + 1, star[1] + 1, star[2])
                    for dx in range(-star[2] + 1, star[2]):
                        for dy in range(-star[2] + 1, star[2]):
                            if grid[i + dx][j + dy] == '*':
                                grid[i + dx][j + dy] = '.'
        return

    solve()


if __name__ == "__main__":
    main()