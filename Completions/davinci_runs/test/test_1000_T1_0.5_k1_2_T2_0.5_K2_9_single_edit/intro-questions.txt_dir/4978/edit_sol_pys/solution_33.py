

n, m = [int(i) for i in input().split()] #input the number of rows and columns

grid = [] #initialize the grid
for i in range(n):
    grid.append(input())

#check the grid
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'V': #if the current position is a V
            if i-1 >= 0: #if the row above exists
                if grid[i-1][j] == '.': #if the row above is a .
                    grid[i-1] = grid[i-1][:j] + "V" + grid[i-1][j+1:] #change the . to a V
                if grid[i-1][j] == '#': #if the row above is a #
                    if (j-1 >= 0) and (grid[i][j-1] == '.'): #if the column to the left is a .
                        grid[i] = grid[i][:j-1] + "V" + grid[i][j:] #change the . to a V
                    if (j+1 < m) and (grid[i][j+1] == '.'): #if the column to the right is a .
                        grid[i] = grid[i][:j+1] + "V" + grid[i][j+2:] #change the . to a V

for i in range(n):
    print(grid[i])
