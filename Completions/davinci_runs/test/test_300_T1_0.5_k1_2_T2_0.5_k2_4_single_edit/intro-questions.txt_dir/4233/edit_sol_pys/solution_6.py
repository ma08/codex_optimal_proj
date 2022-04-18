

def check(grid,i,j,r,n,m):
    if (i-r<0 or j-r<0 or i+r>=n or j+r>=m):
        return False
    else:
        if (grid[i-r][j-r] == '*' and grid[i-r][j+r] == '*' and grid[i+r][j-r] == '*' and grid[i+r][j+r] == '*'):
            return True
        else:
            return False


def main():
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    flag = False
    stars = []
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == '*'):
                if (i>0 and j>0 and grid[i-1][j-1] == '*') or (i>0 and grid[i-1][j] == '*') or (i>0 and j<m-1 and grid[i-1][j+1] == '*') or (j>0 and grid[i][j-1] == '*') or (j<m-1 and grid[i][j+1] == '*') or (i<n-1 and j>0 and grid[i+1][j-1] == '*') or (i<n-1 and grid[i+1][j] == '*') or (i<n-1 and j<m-1 and grid[i+1][j+1] == '*'):
                    flag = True
                    r = 1
                    while(flag):
                        if (check(grid,i,j,r,n,m)):
                            r += 1
                        else:
                            flag = False
                    stars.append([i+1,j+1,r-1])
                else:
                    flag = True
                    r = 1
                    while(flag):
                        if (check(grid,i,j,r,n,m)):
                            r += 1
                        else:
                            flag = False
                    stars.append([i+1,j+1,r-1])
    if (len(stars) == 0):
        print("-1")
    else:
        print(len(stars))
        for i in range(len(stars)):
            print(stars[i][0],stars[i][1],stars[i][2])
main()
