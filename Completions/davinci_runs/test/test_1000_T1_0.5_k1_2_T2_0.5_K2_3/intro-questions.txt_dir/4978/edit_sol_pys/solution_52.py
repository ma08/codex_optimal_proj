

def main():
    n,m = map(int,input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    #print(grid) # debug
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'V':
                grid[i][j] = 'v'
    #print(grid) # debug
    while True:
        changed = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'v':
                    if i > 0 and grid[i-1][j] == '.':
                        grid[i-1][j] = 'v'
                        changed = True
                    if i < n-1 and grid[i+1][j] == '.':
                        grid[i+1][j] = 'v'
                        changed = True
                    if j < m-1 and grid[i][j+1] == ".":
                        grid[i][j+1] = "v"
                        changed = True
                    if j > 0 and grid[i][j-1] == ".":
                        grid[i][j-1] = "v"
                        changed = True
        if not changed:
            break
    #print(grid) # debug
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "v":
                grid[i][j] = "V"
            elif grid[i][j] == ".":
                grid[i][j] = " "
    #print(grid) # debug
    for i in range(n):
        print("".join(grid[i]))

if __name__ == "__main__":
    main()
