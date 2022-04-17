

def main():
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    stars = []
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == '*'): #if the current point is a star
                if (i>0 and j>0 and grid[i-1][j-1] == '*') or (i>0 and grid[i-1][j] == '*') or (i>0 and j<m-1 and grid[i-1][j+1] == '*') or (j>0 and grid[i][j-1] == '*') or (j<m-1 and grid[i][j+1] == '*') or (i<n-1 and j>0 and grid[i+1][j-1] == '*') or (i<n-1 and grid[i+1][j] == '*') or (i<n-1 and j<m-1 and grid[i+1][j+1] == '*'): #if the star has a neighbor
                    stars.append([i+1,j+1,1])
                else: #if the star has no neighbor
                    flag = True
                    r = 0
                    while(flag):
                        r += 1
                        if (i-r<0 or j-r<0 or i+r>=n or j+r>=m): #if the star is at the edge of the grid
                            flag = False
                        else:
                            if (grid[i-r][j-r] == '*' and grid[i-r][j+r] == '*' and grid[i+r][j-r] == '*' and grid[i+r][j+r] == '*'): #if the star has 4 neighbors
                                stars.append([i+1,j+1,r+1])
                            else: #if the star does not have 4 neighbors
                                flag = False
    if (len(stars) == 0): #if there are no stars
        print("-1")
    else: #if there are stars
        print(len(stars))
        for i in range(len(stars)):
            print(stars[i][0],stars[i][1],stars[i][2])
main()
