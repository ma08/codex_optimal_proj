
def main():
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    stars = []
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == '*'):
                if (i>0 and j>0 and grid[i-1][j-1] == '*') or (i>0 and grid[i-1][j] == '*') or (i>0 and j<m-1 and grid[i-1][j+1] == '*') or (j>0 and grid[i][j-1] == '*') or (j<m-1 and grid[i][j+1] == '*') or (i<n-1 and j>0 and grid[i+1][j-1] == '*') or (i<n-1 and grid[i+1][j] == '*') or (i<n-1 and j<m-1 and grid[i+1][j+1] == '*'):
                    stars.append([i+1, j+1, 1])
                else:
                    flag = True
                    radius = 0
                    while(flag):
                        radius += 1
                        if (i-radius<0 or j-radius<0 or i+radius>=n or j+radius>=m):
                            flag = False
                        else:
                            if (grid[i-radius][j-radius] == '*' and grid[i-radius][j+radius] == '*' and grid[i+radius][j-radius] == '*' and grid[i+radius][j+radius] == '*'):
                                stars.append([i+1, j+1, radius+1])
                            else:
                                flag = False
    if (len(stars) == 0):
        print("-1")
    else:
        print(len(stars))
        for i in range(len(stars)):
            print(stars[i][0], stars[i][1], stars[i][2])
main()
