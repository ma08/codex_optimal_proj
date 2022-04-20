


def main():
    n,m = list(map(int, input().split()))
    grid = []
    for i in range(n):
        grid.append(list(input()))
    stars = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars += 1
                for k in range(j+1, m):
                    if grid[i][k] == '*':
                        continue
                    else:
                        break

    print(stars)
    return


if __name__ == '__main__':
    main()